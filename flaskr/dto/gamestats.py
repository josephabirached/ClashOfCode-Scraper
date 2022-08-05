from dataclasses import dataclass
from datetime import time
from typing import Optional

@dataclass
class GameStats:
    username: str
    userId: str
    university: Optional[str]
    ranking: str
    score: int
    gameTime: time
    programmingLang: str
    codeLength: Optional[int]