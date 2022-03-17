def main():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    clock = pygame.time.Clock()

    from game import Game

    game = Game(screen) 

    while game.gamestate == ConfigAndStates.GameState.RUNNING:
        clock.tick(ConfigAndStates.FPS)
        game.update()
        pygame.display.flip()
    
    return

if __name__ == "__main__":
    main()
