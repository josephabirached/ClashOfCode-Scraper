import datetime
from datetime import datetime as dt
from .dto.gamestats import GameStats
from .dto.playerstats import PlayerStats
from flask import jsonify 
import pandas as pd
from . import db

class PlayerService:
    def __init__(self) -> None:
        pass

    def get_player_statistics(self, playerGameScore:list[GameStats]):

        playerName = playerGameScore[0].username
        playerId = playerGameScore[0].userId
        gamesPlayed = len(playerGameScore)
        
        averageRank = 0
        averageScore = 0
        averageCode = 0
        languages = []
        totalSeconds = 0

        for game in playerGameScore:
            averageRank += game.ranking    
            averageScore += game.score
            averageCode += 0 if game.codeLength == None else game.codeLength              
            if game.programmingLang not in languages:
                languages.append(game.programmingLang)
            h, m, s = game.gameTime.split(':')
            totalSeconds += int(h)*60*60 + int(m)*60 + int(s)

        averageRank = round(averageRank/gamesPlayed, 2)
        averageScore = round(averageScore/gamesPlayed, 2)
        averageCode = round(averageCode/gamesPlayed, 2) if averageCode != 0 else None

        return jsonify(
            PlayerStats(playerName,
            playerId,
            game.university,
            gamesPlayed,
            averageRank,
            averageScore,averageCode,
            str(datetime.timedelta(seconds=(totalSeconds/gamesPlayed))).split('.')[0],
            languages))
        
    def update_player_university(self, file):
        data = pd.read_csv(file)

        data = data[data['university'].notna()]

        for index, row in data.iterrows():
            db.updatePlayer(row['university'], row['web-scraper-start-url'].split('/')[-1])