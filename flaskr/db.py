import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
import pandas as pd


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # Initialize the DB with the tables
    with current_app.open_resource('..\\database\\schema.sql') as f:
        db.executescript(f.read().decode("utf-8"))

    # Initialize the DB with the Data.
    data =  pd.read_csv("database\\data.csv")

    # First we get the profiles with their unique profile link
    dataProfiles = data.drop_duplicates(subset= ["profileLink-href"])
    for index, row in dataProfiles.iterrows():
        db.execute(
            """INSERT INTO player(username, userId) VALUES(?,?);""",
            (row['name'],row['profileLink-href'].split('/')[-1])
            )

    db.commit()

    # Inserting the Games data
    for index, row in data.iterrows():
        profileId =  db.execute("""SELECT id FROM player WHERE userId=?;""", (row['profileLink-href'].split('/')[-1],)).fetchone()[0]

        db.execute(
            """INSERT INTO gameScore(gameUrl, ranking, score, gameTime, programmingLang, codeLength, playerId) VALUES(?,?,?,?,?,?,?);""",
            (row['web-scraper-start-url'].split('/')[-1],row['profileLink'], int(row['score'][:-1]) ,row['time'],row['language'],row['length'],profileId)
            )

    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def getPlayerGamesByName(playerName):
    conn = get_db()
    playerGames = conn.execute("""
        SELECT username,userid,ranking, score, gameTime, programmingLang, codeLength
        FROM player p, gameScore g
        WHERE p.username == ? COLLATE NOCASE
        AND p.id == g.playerId
    """, (playerName,)).fetchall()

    return playerGames

def getPlayerGamesById(playerId):
    conn = get_db()
    playerGames = conn.execute("""
        SELECT username,userid,ranking, score, gameTime, programmingLang, codeLength
        FROM player p, gameScore g
        WHERE p.userId == ? COLLATE NOCASE
        AND p.id == g.playerId
    """, (playerId,)).fetchall()

    return playerGames