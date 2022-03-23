def main():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    CLOCK = pygame.time.Clock()

    from game import Game

    game = Game(screen, CLOCK)
    game.start()
    
    if game.gamestate == ConfigAndStates.GameState.CRASHED:
        raise Exception("Game has Crashed")

    return

def debug():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    CLOCK = pygame.time.Clock()

    from game import Game

    game = Game(screen, CLOCK)
    game.clean(screen, CLOCK)
    game.set_up("perf_test_map")
    game.start()
    
    if game.gamestate == ConfigAndStates.GameState.CRASHED:
        raise Exception("Game has Crashed")

    return

if __name__ == "__main__":
    main()
