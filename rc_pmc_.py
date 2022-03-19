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

PLAYER_ANIMATOR = {
    "down": {
        "fixed": pygame.transform.scale(pygame.image.load('assets/imgs/player/front/fixed.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
        "animated": [
            pygame.transform.scale(pygame.image.load('assets/imgs/player/front/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/front/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/front/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/front/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
        ]
    },
    "up": {
        "fixed": pygame.transform.scale(pygame.image.load('assets/imgs/player/back/fixed.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
        "animated": [
            pygame.transform.scale(pygame.image.load('assets/imgs/player/back/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/back/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/back/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/back/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
        ]
    },
    "left": {
        "fixed": pygame.transform.scale(pygame.image.load('assets/imgs/player/left/fixed.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
        "animated": [
            pygame.transform.scale(pygame.image.load('assets/imgs/player/left/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/left/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/left/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/left/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
        ]
    },
    "right": {
        "fixed": pygame.transform.scale(pygame.image.load('assets/imgs/player/right/fixed.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
        "animated": [
            pygame.transform.scale(pygame.image.load('assets/imgs/player/right/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/right/left.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/right/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
            pygame.transform.scale(pygame.image.load('assets/imgs/player/right/right.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
        ]
    }
}

class Player(RenderedComponent_OnMap):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.positions = [x_pos, y_pos]
        self.dir = "down"
        self.current = "fixed"
        self.astate = 0
        self.image = PLAYER_ANIMATOR[self.dir][self.current]
        self.rect = pygame.Rect(self.positions[0]*ConfigAndStates.SCALE,self.positions[1]*ConfigAndStates.SCALE,ConfigAndStates.SCALE,ConfigAndStates.SCALE)
    
    def update(self):
        print("player updated")
    
    def rotate(self, new_dir):
        self.dir = new_dir
    
    def change_state(self, new_state):
        if self.current == "fixed":
            if new_state == "animated":
                self.current = new_state
                self.astate = 0
        elif self.current == "animated":
            if new_state == "fixed":
                self.current = new_state
                self.astate = 0

    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        if self.current == "fixed":
            self.image = PLAYER_ANIMATOR[self.dir][self.current]
            self.rect = pygame.Rect(self.positions[0]*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),self.positions[1]*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
            screen.blit(self.image, self.rect)
        else:
            self.image = PLAYER_ANIMATOR[self.dir][self.current][self.astate]
            self.rect = pygame.Rect(self.positions[0]*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),self.positions[1]*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
            screen.blit(self.image, self.rect)
            self.astate = (self.astate + 1) % 4
        return RenderSucces()
    
    def update_position(self, pos_moves: tuple[int, int]):
        self.positions[0] = pos_moves[0]
        self.positions[1] = pos_moves[1]

MAPS_TILES_IMAGES = {
    "G": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/grass/grass0.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
    "H": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/grass/grass1.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
    "W": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/water/water.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
    "R": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_cross.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
    "S": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_line.png').convert_alpha(), ConfigAndStates.SCALE_GROUP),
    "T": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/roads/road_column.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
}

MAPS_LAYER_TILES_IMAGES = {
    "G": pygame.transform.scale(pygame.image.load('assets/imgs/tiles/grass/grass_contain.png').convert_alpha(), ConfigAndStates.SCALE_GROUP)
}

class Map(RenderedComponent_OnMap):
    def __init__(self, path: str):
        super().__init__()
        self.map: list[list[str]] = []
        self.layer: list[list[str]] = []
        with open(ConfigAndStates.MAPS_PATH + 'base/' + path + ConfigAndStates.MAPS_EXT, 'r') as map_file:
            for line in map_file.readlines():
                temp = []
                for i in range(0, len(line) - 1):
                    temp.append(line[i])
                self.map.append(temp.copy())
        try:
            with open(ConfigAndStates.MAPS_PATH + 'layer/' + path + ConfigAndStates.MAPS_EXT, 'r') as map_layer_file:
                for line in map_layer_file.readlines():
                    temp = []
                    for i in range(0, len(line) - 1):
                        temp.append(line[i])
                    self.layer.append(temp.copy())
        except:
            self.layer = []
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        y_pos = 0
        for line in self.map:
            if y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) >= 0 and y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[1]:
                x_pos = 0
                for tile in line:
                    if x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) >= 0 and x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[0]:
                        rect = pygame.Rect(x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
                        image = MAPS_TILES_IMAGES[tile]
                        screen.blit(image, rect)
                    x_pos += 1
            y_pos += 1
        if len(self.layer) != 0:
            y_pos = 0
            for line in self.layer:
                if y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) >= 0 and y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[1]:
                    x_pos = 0
                    for tile in line:
                        if tile != ' ':
                            if x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) >= 0 and x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE) < ConfigAndStates.SCREEN_SIZE[0]:
                                rect = pygame.Rect(x_pos*ConfigAndStates.SCALE - (x_axis * ConfigAndStates.SCALE),y_pos*ConfigAndStates.SCALE - (y_axis * ConfigAndStates.SCALE),ConfigAndStates.SCALE,ConfigAndStates.SCALE)
                                image = MAPS_LAYER_TILES_IMAGES[tile]
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
