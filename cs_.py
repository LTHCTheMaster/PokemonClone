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
MAP_TILES_COLLISION = ("baseW")
MAP_TILES_GRASS = ("baseG", "baseH")
MAP_TILES_ROAD = ("baseR", "baseS", "baseT")

###################################################""

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2
