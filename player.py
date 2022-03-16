import pygame
import config

class Player:
    def __init__(self, x_pos, y_pos):
        self.positions = [x_pos, y_pos]
        self.image = pygame.image.load('assets/imgs/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.positions[0]*config.SCALE,self.positions[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update(self):
        print("player updated")
    
    def render(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
    
    def update_position(self, pos_x: int, pos_y: int):
        self.positions = [self.positions[0] + pos_x, self.positions[1] + pos_y]
        self.rect = pygame.Rect(self.positions[0]*config.SCALE,self.positions[1]*config.SCALE,config.SCALE,config.SCALE)
