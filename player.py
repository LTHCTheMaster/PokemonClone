import pygame
import configuration

class Player:
    def __init__(self, x_pos, y_pos):
        self.positions = [x_pos, y_pos]
        self.image = pygame.image.load('assets/imgs/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (configuration.SCALE, configuration.SCALE))
        self.rect = pygame.Rect(self.positions[0]*configuration.SCALE,self.positions[1]*configuration.SCALE,configuration.SCALE,configuration.SCALE)
    
    def update(self):
        print("player updated")
    
    def render(self, screen: pygame.Surface, x_axis: int, y_axis: int):
        self.rect = pygame.Rect(self.positions[0]*configuration.SCALE - (x_axis * configuration.SCALE),self.positions[1]*configuration.SCALE - (y_axis * configuration.SCALE),configuration.SCALE,configuration.SCALE)
        screen.blit(self.image, self.rect)
    
    def update_position(self, pos_moves: list[int]):
        self.positions = [self.positions[0] + pos_moves[0], self.positions[1] + pos_moves[1]]
