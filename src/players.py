from enum import Enum

class Player:
    def __init__(self, name, position, player_type):
        self.name     = name
        self.position = position
        self.player_type = player_type

class Position(Enum):
    QB = 1
    RB = 2
    WR = 3
    TE = 4
    D  = 5
    K  = 6

class PlayerType(Enum):
    keeper  = 1
    veteran = 2
    youngin = 3
    rookie  = 4
    cuff    = 5
    na      = 6