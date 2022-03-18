from enum import Enum

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window Size
SCREEN_SIZE = (640,480)

# FPS
FPS = 50

# Other
SCALE = 32
LOGS_PATH = 'logs/'
LOGS_EXT = '.log'

# Tiles
MAP_TILES_COLLISION = ("baseW")
MAP_TILES_GRASS = ("baseG", "baseH")
MAP_TILES_ROAD = ("baseR", "baseS", "baseT")

###################################################""

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2,
    CRASHED = 3

class LogState(Enum):
    NONE = 0,
    SUCCES = 1,
    FAILURE = 2

class InstanceState(Enum):
    NONE = 0,
    ON_MAP = 1

class ResultState:
    def __init__(self):
        pass
