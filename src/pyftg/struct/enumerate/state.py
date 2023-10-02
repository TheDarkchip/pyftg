from enum import Enum

class State(Enum):
    STAND = 0
    CROUCH = 1
    AIR = 2
    DOWN = 3

    def __str__(self):
        return self.name