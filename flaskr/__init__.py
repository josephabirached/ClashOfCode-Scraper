import os
from flask import Flask, request
from flaskr.dto.gamestats import GameStats
from flaskr.playerservice import PlayerService
from . import db
import json
import pandas as pd

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/player', methods=['GET'])
    def getPlayerStatistics():
        args = request.args
        playerName = args.get('playerName')
        playerId = args.get('playerId')

        if(playerName != None):
            playerGames = db.getPlayerGamesByName(playerName)
        elif(playerId != None):
            playerGames = db.getPlayerGamesById(playerId)
        else:
            return "You must specify the playerName or playerId", 400

        if playerGames == None or len(playerGames) == 0:
            return "Not found", 404

        return PlayerService().get_player_statistics([GameStats(game[0],game[1],game[2],game[3],game[4],game[5],game[6],game[7]) for game in playerGames])

    @app.route('/players', methods=['GET', 'POST'])
    def getAllPlayers():
        if request.method == 'GET':
            profileUrls = ["https://www.codingame.com/profile/"+row[0] for row in db.getAll()] 
            
            with open('./scraper/university-site-map.json') as file:
                data = json.load(file)
                data["startUrl"] = profileUrls
                return data

        if request.method == 'POST':
            if 'file' not in request.files:
                return 'No selected file', 400
            
            file = request.files['file']

            if file.filename == '':
                return 'No selected file', 400

            if file.content_type != 'text/csv':
                return 'Only CSV files allowed', 400
            
            PlayerService().update_player_university(file)

            return '', 201

    return app