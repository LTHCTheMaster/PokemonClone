import configuration
from map import Map
from player import Player
from math import ceil

class Camera:
    def __init__(self, pos_x, pos_y):
        self.positions = [pos_x, pos_y]
    
    def determine_camera(self, map: Map, player: Player):
        map_size = map.get_size()

        max_x_pos = map_size[0] + 1 - configuration.SCREEN_SIZE[0] / configuration.SCALE
        x_pos = player.positions[0] - ceil(round(configuration.SCREEN_SIZE[0]/configuration.SCALE/2))

        if x_pos <= max_x_pos and x_pos >= 0:
            self.positions[0] = x_pos
        elif x_pos < 0:
            self.positions[0] = 0
        else:
            self.positions[0] = max_x_pos

        max_y_pos = map_size[1] + 1 - configuration.SCREEN_SIZE[1] / configuration.SCALE
        y_pos = player.positions[1] - ceil(round(configuration.SCREEN_SIZE[1]/configuration.SCALE/2))

        if y_pos <= max_y_pos and y_pos >= 0:
            self.positions[1] = y_pos
        elif y_pos < 0:
            self.positions[1] = 0
        else:
            self.positions[1] = max_y_pos
    
    def get_pos(self) -> tuple[int, int]:
        return (self.positions[0], self.positions[1])
