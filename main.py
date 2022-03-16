import pygame
import config
from game_state import GameState

pygame.init()
screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption('Pokemon Clone')

clock = pygame.time.Clock()

from game import Game

game = Game(screen) 

while game.game_state == GameState.RUNNING:
    clock.tick(config.FPS)
    game.update()
    pygame.display.flip()
