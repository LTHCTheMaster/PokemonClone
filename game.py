import pygame
from player import Player
from game_state import GameState
import config

map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load('assets/imgs/grass0.png').convert_alpha(), (config.SCALE, config.SCALE)),
    "H": pygame.transform.scale(pygame.image.load('assets/imgs/grass1.png').convert_alpha(), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load('assets/imgs/water.png').convert_alpha(), (config.SCALE, config.SCALE))
}

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.objects: list = []
        self.game_state = GameState.NONE
        self.map = []
        self.set_up()
    
    def set_up(self):
        player = Player(1, 1)
        self.player = player

        self.objects.append(self.player)

        self.game_state = GameState.RUNNING
        
        self.load_map("01")
    
    def load_map(self, map: str):
        with open('assets/maps/' + map + '.txt', 'r') as map_file:
            for line in map_file.readlines():
                temp = []
                for i in range(0, len(line) - 1):
                    temp.append(line[i])
                self.map.append(temp.copy())

    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()
        self.render_map()
        for object in self.objects:
            object.render(self.screen)

    def render_map(self):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos*config.SCALE,y_pos*config.SCALE,config.SCALE,config.SCALE)
                self.screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_z:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_s:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_q:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_d:
                    self.player.update_position(1, 0)
