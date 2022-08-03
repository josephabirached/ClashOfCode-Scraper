from dataclasses import dataclass
from datetime import time
from typing import Optional

@dataclass
class PlayerStats:
    name: str
    codingGameId: str
    gamesPlayed: int
    averageRank: int
    averageScore: int
    averageCodeLength: Optional[int]
    averageGameTime: time
    programmingLanguageUsed: list[str]
