DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS gameScore;

CREATE TABLE player
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    userId TEXT UNIQUE NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gameScore
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gameUrl TEXT NOT NULL,
    ranking INT NOT NULL,
    score INT NOT NULL,
    gameTime TIME NOT NULL,
    programmingLang TEXT,
    codeLength INT,
    playerId INT NOT NULL,
    FOREIGN KEY (playerId) REFERENCES player(id)
);