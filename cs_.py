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

# Tiles
MAP_TILES_COLLISION = ("W")
MAP_TILES_GRASS = ("G", "H")
MAP_TILES_ROAD = ("R", "S", "T")

###################################################""

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2
