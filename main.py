def main():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    clock = pygame.time.Clock()

    from game import Game

    game = Game(screen, clock)
    game.loop()
    
    return

if __name__ == "__main__":
    main()
