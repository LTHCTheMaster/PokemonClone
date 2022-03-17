import pygame
import configuration

map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load('assets/imgs/grass0.png').convert_alpha(), (configuration.SCALE, configuration.SCALE)),
    "H": pygame.transform.scale(pygame.image.load('assets/imgs/grass1.png').convert_alpha(), (configuration.SCALE, configuration.SCALE)),
    "W": pygame.transform.scale(pygame.image.load('assets/imgs/water.png').convert_alpha(), (configuration.SCALE, configuration.SCALE))
}

class Map:
    def __init__(self, path: str):
        self.map: list[list[str]] = []
        with open('assets/maps/' + path + '.txt', 'r') as map_file:
            for line in map_file.readlines():
                temp = []
                for i in range(0, len(line) - 1):
                    temp.append(line[i])
                self.map.append(temp.copy())
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos*configuration.SCALE - (x_axis * configuration.SCALE),y_pos*configuration.SCALE - (y_axis * configuration.SCALE),configuration.SCALE,configuration.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1
    
    def get_at(self, pos_on: list[int]) -> str:
        return self.map[pos_on[1]][pos_on[0]]
    
    def get_size(self) -> tuple[int, int]:
        return (len(self.map[0]) - 1, len(self.map) - 1)
