import pygame
import cs_ as ConfigAndStates
from math import ceil

class RenderSucces(ConfigAndStates.ResultState):
    def __init(self):
        pass

class RenderedComponent:
    def __init__(self):
        pass

    def render(self, screen: pygame.Surface):
        return RenderSucces()

class RenderedComponent_OnMap(RenderedComponent):
    def __init__(self):
        super().__init__()
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        return RenderSucces()

class Player(RenderedComponent_OnMap):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.positions = [x_pos, y_pos]
        self.image = pygame.image.load('assets/imgs/player/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (ConfigAndStates.SCALE, ConfigAndStates.SCALE))
        self.rect = pygame.Rect(self.positions[0]*ConfigAndStates.SCALE,self.positions[1]*ConfigAndStates.SCALE,ConfigAndStates.SCALE,ConfigAndStates.SCALE)
    
    def update(self):
        print("player updated")
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        self.rect = pygame.Rect(self.positions[0]*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),self.positions[1]*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
        screen.blit(self.image, self.rect)
        return RenderSucces()
    
    def update_position(self, pos_moves: tuple[int, int]):
        self.positions[0] = pos_moves[0]
        self.positions[1] = pos_moves[1]

MAPS_TILES_IMAGES = {
    "G": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/grass/grass0.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE)),
    "H": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/grass/grass1.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE)),
    "W": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/water/water.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE)),
    "R": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_cross.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE)),
    "S": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_line.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE)),
    "T": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_column.png').convert_alpha(), (ConfigAndStates.SCALE, ConfigAndStates.SCALE))
}

class Map(RenderedComponent_OnMap):
    def __init__(self, path: str):
        super().__init__()
        self.map: list[list[str]] = []
        with open('assets/maps/base/' + path + '.txt', 'r') as map_file:
            for line in map_file.readlines():
                temp = []
                for i in range(0, len(line) - 1):
                    temp.append('base'+line[i])
                self.map.append(temp.copy())
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        y_pos = 0
        for line in self.map:
            if y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) >= 0 and y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[1]:
                x_pos = 0
                for tile in line:
                    if "base" in tile:
                        if x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) >= 0 and x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[0]:
                            image = MAPS_TILES_IMAGES[tile.replace('base','')]
                            rect = pygame.Rect(x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
                            screen.blit(image, rect)
                    x_pos += 1
            y_pos += 1
        return RenderSucces()
    
    def get_at(self, pos_on: list[int]) -> str:
        return self.map[pos_on[1]][pos_on[0]]
    
    def get_size(self) -> tuple[int, int]:
        return (len(self.map[0]) - 1, len(self.map) - 1)

class Camera:
    def __init__(self, pos_x, pos_y):
        self.positions = [pos_x, pos_y]
    
    def determine_camera(self, map: Map, player: Player):
        map_size = map.get_size()

        max_x_pos = map_size[0] + 1 - ConfigAndStates.SCREEN_SIZE[0] / ConfigAndStates.SCALE
        x_pos = player.positions[0] - ceil(round(ConfigAndStates.SCREEN_SIZE[0]/ConfigAndStates.SCALE/2))

        if x_pos <= max_x_pos and x_pos >= 0:
            self.positions[0] = x_pos
        elif x_pos < 0:
            self.positions[0] = 0
        else:
            self.positions[0] = max_x_pos

        max_y_pos = map_size[1] + 1 - ConfigAndStates.SCREEN_SIZE[1] / ConfigAndStates.SCALE
        y_pos = player.positions[1] - ceil(round(ConfigAndStates.SCREEN_SIZE[1]/ConfigAndStates.SCALE/2))

        if y_pos <= max_y_pos and y_pos >= 0:
            self.positions[1] = y_pos
        elif y_pos < 0:
            self.positions[1] = 0
        else:
            self.positions[1] = max_y_pos
    
    def get_pos(self) -> tuple[int, int]:
        return (self.positions[0], self.positions[1])
