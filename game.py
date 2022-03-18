import pygame
from rc_pmc_ import Player, Map, Camera, RenderSucces
import cs_ as ConfigAndStates
from logger_ import Logger

SUPPORTED_OBJECTS = list[Player | Map]

class EventsHandler:
    def __init__(self, player: Player, map: Map, camera: Camera, objects: SUPPORTED_OBJECTS, gamestate: ConfigAndStates.GameState):
        self.player = player
        self.map = map
        self.camera = camera
        self.objects = objects
        self.gamestate = gamestate
        self.player_has_moved = False
    
    def handle_events_on_map(self) -> ConfigAndStates.GameState:
        try:
            self.player_has_moved = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = ConfigAndStates.GameState.ENDED
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = ConfigAndStates.GameState.ENDED
                    else:
                        self.handle_playerActionsEvent(event)
        except:
            self.gamestate = ConfigAndStates.GameState.CRASHED
        return self.gamestate

    def handle_playerActionsEvent(self, event: pygame.event.Event):
        self.handle_moveEvent(event)

    def handle_moveEvent(self, event: pygame.event.Event):
        if event.key in (pygame.K_z, pygame.K_w):
            self.move_object(self.player, (0, -1))
        elif event.key == pygame.K_s:
            self.move_object(self.player, (0, 1))
        elif event.key in (pygame.K_q, pygame.K_a):
            self.move_object(self.player, (-1, 0))
        elif event.key == pygame.K_d:
            self.move_object(self.player, (1, 0))

    def move_object(self, object: Player, pos_moves: tuple[int, int]):
        new_pos = (object.positions[0] + pos_moves[0], object.positions[1] + pos_moves[1])

        map_size = self.map.get_size()
        if new_pos[0] < 0 or new_pos[0] > map_size[0] or new_pos[1] < 0 or new_pos[1] > map_size[1]:
            return
        if self.map.get_at(new_pos) in ConfigAndStates.MAP_TILES_COLLISION:
            return
        
        self.player_has_moved = True

        object.update_position(new_pos)

class Renderer:
    def __init__(self, screen: pygame.Surface, player: Player, map: Map, camera: Camera, objects_map: SUPPORTED_OBJECTS, state = ConfigAndStates.GameState):
        self.screen = screen
        self.player = player
        self.map = map
        self.camera = camera
        self.objects_map = objects_map
        self.state = state
    
    def render_on_map(self) -> ConfigAndStates.GameState:
        self.camera.determine_camera(self.map, self.player)
        cam_pos = self.camera.get_pos()
        for object in self.objects_map:
            try:
                if type(object.render(self.screen, cam_pos[0], cam_pos[1])) is RenderSucces:
                    pass
                else:
                    self.state = ConfigAndStates.GameState.CRASHED
            except:
                self.state = ConfigAndStates.GameState.CRASHED
        return self.state

class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, logger: Logger):
        self.screen: pygame.Surface = screen
        self.objects_map: SUPPORTED_OBJECTS = []
        self.gamestate = ConfigAndStates.GameState.NONE
        self.map: Map = None
        self.camera = Camera(0,0)
        self.clock = clock
        self.logger = logger
        self.current_sys_state = ConfigAndStates.InstanceState.NONE
        self.set_up()
    
    def set_up(self):
        map_loaded = Map("01")
        self.map = map_loaded

        player = Player(1, 1)
        self.player = player

        self.objects_map.extend([self.map, self.player])

        self.gamestate = ConfigAndStates.GameState.RUNNING
        self.renderer = Renderer(self.screen, self.player, self.map, self.camera, self.objects_map, self.gamestate)
        self.current_sys_state = ConfigAndStates.InstanceState.ON_MAP
        self.event_handler = EventsHandler(self.player, self.map, self.camera, self.objects_map, self.gamestate)

    def update(self):
        if self.current_sys_state == ConfigAndStates.InstanceState.ON_MAP:
            self.gamestate = self.event_handler.handle_events_on_map()
            if self.gamestate == ConfigAndStates.GameState.RUNNING:
                self.gamestate = self.renderer.render_on_map()
        pygame.display.flip()
    
    def loop(self):
        self.logger.log('[Game]: Require the start of the loop of the game')
        while self.gamestate == ConfigAndStates.GameState.RUNNING:
            self.clock.tick(ConfigAndStates.FPS)
            self.update()
        self.logger.log('[Game]: Require the end of the game')
        return
