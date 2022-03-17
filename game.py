import pygame
from pmc_ import Player, Map, Camera
import cs_ as ConfigAndStates

SUPPORTED_OBJECTS = list

class EventsHandler:
    def __init__(self, player: Player, map: Map, camera: Camera, objects: SUPPORTED_OBJECTS, gamestate: ConfigAndStates.GameState):
        self.player = player
        self.map = map
        self.camera = camera
        self.objects = objects
        self.gamestate = gamestate
    
    def handle_events(self) -> ConfigAndStates.GameState:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gamestate = ConfigAndStates.GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gamestate = ConfigAndStates.GameState.ENDED
                else:
                    self.handle_moveEvent(event)
        return self.gamestate
    
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
        if self.map.get_at(new_pos) == "W":
            return
        
        object.update_position(new_pos)

class Renderer:
    def __init__(self, screen: pygame.Surface, player: Player, map: Map, camera: Camera, objects: SUPPORTED_OBJECTS):
        self.screen = screen
        self.player = player
        self.map = map
        self.camera = camera
        self.objects = objects
    
    def render(self):
        self.camera.determine_camera(self.map, self.player)
        cam_pos = self.camera.get_pos()
        self.map.render(self.screen, cam_pos[0], cam_pos[1])
        self.player.render(self.screen, cam_pos[0], cam_pos[1])
        for object in self.objects:
            object.render(self.screen)

class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        self.screen: pygame.Surface = screen
        self.objects: SUPPORTED_OBJECTS = []
        self.gamestate = ConfigAndStates.GameState.NONE
        self.map: Map = None
        self.camera = Camera(0,0)
        self.clock = clock
        self.set_up()
    
    def set_up(self):
        map_loaded = Map("01")
        self.map = map_loaded

        player = Player(1, 1)
        self.player = player

        self.renderer = Renderer(self.screen, self.player, self.map, self.camera, self.objects)
        self.gamestate = ConfigAndStates.GameState.RUNNING
        self.event_handler = EventsHandler(self.player, self.map, self.camera, self.objects, self.gamestate)

    def update(self):
        self.screen.fill(ConfigAndStates.BLACK)
        self.gamestate = self.event_handler.handle_events()
        self.renderer.render()
        pygame.display.flip()
    
    def loop(self):
        while self.gamestate == ConfigAndStates.GameState.RUNNING:
            self.clock.tick(ConfigAndStates.FPS)
            self.update()
        return
