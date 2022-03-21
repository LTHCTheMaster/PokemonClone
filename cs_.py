from enum import Enum

# Colors
BLACK = (0, 0, 0)
LIGHT_GREY = (225, 225, 225)

# Window Size
SCREEN_SIZE = (640,480)

# FTPS
FTPS = 60

# Other
SCALE = 32
SCALE_GROUP = (SCALE, SCALE)
MAPS_PATH = 'assets/maps/'
MAPS_EXT = '.txt'

# Tiles
MAP_TILES_COLLISION = ("W")
MAP_TILES_GRASS = ("G", "H")
MAP_TILES_ROAD = ("R", "S", "T")
MAP_TILES_WILD_ENCOUNTER = ("G")

###################################################""

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2,
    CRASHED = 3

class InstanceState(Enum):
    NONE = 0,
    ON_MAP = 1,
    IN_WILD_BATTLE = 2

class ResultState:
    def __init__(self):
        pass
