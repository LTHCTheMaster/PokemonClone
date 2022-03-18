def main():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    clock = pygame.time.Clock()

    from game import Game
    from logger_ import Logger

    logger = Logger()
    if logger.state == ConfigAndStates.LogState.FAILURE:
        raise Exception("Failure on the logger")

    game = Game(screen, clock, logger)
    logger.log('[INIT]: Game Instance Initialized')
    game.loop()
    
    if game.gamestate == ConfigAndStates.GameState.CRASHED:
        logger.log('[CRASH]: Game has Crashed')
        raise Exception("Game has Crashed")

    logger.log('[Game]: Game successfully ended')
    return

def debug():
    import pygame
    import cs_ as ConfigAndStates

    pygame.init()
    screen = pygame.display.set_mode(ConfigAndStates.SCREEN_SIZE)
    pygame.display.set_caption('Pokemon Clone')

    clock = pygame.time.Clock()

    from game import Game
    from logger_ import Logger

    logger = Logger()
    if logger.state == ConfigAndStates.LogState.FAILURE:
        raise Exception("Failure on the logger")

    game = Game(screen, clock, logger)
    game.clean(screen, clock, logger)
    game.set_up("perf_test_map")
    logger.log('[INIT]: Game Instance Initialized')
    game.loop()
    
    if game.gamestate == ConfigAndStates.GameState.CRASHED:
        logger.log('[CRASH]: Game has Crashed')
        raise Exception("Game has Crashed")

    logger.log('[Game]: Game successfully ended')
    return

if __name__ == "__main__":
    main()
