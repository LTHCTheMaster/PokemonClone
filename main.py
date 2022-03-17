import pygame
import configuration
from gamestate import GameState

pygame.init()
screen = pygame.display.set_mode(configuration.SCREEN_SIZE)
pygame.display.set_caption('Pokemon Clone')

clock = pygame.time.Clock()

from game import Game

game = Game(screen) 

while game.gamestate == GameState.RUNNING:
    clock.tick(configuration.FPS)
    game.update()
    pygame.display.flip()
