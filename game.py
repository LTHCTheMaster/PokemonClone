import pygame
from rc_pmc_ import Player, Map, Camera, RenderSucces, RenderedComponent
import cs_ as ConfigAndStates
from random import random

SUPPORTED_OBJECTS = list[Player | Map]

class EventsHandler:
    def __init__(self, player: Player, map: Map, camera: Camera, objects: SUPPORTED_OBJECTS, gamestate: ConfigAndStates.GameState, game):
        self.player = player
        self.map = map
        self.camera = camera
        self.objects = objects
        self.gamestate = gamestate
        self.player_has_moved = False
        self.player_ismoving = False
        self.player_dir = "up"
        self.player_move_frame = 0
        self.game = game
    
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
                elif event.type == pygame.KEYUP:
                    self.player_ismoving = False
                    self.player_move_frame = 0
            self.execute_move()
            self.can_wild_battle()
        except:
            self.gamestate = ConfigAndStates.GameState.CRASHED
        return self.gamestate

    def handle_playerActionsEvent(self, event: pygame.event.Event):
        self.handle_moveEvent(event)

    def handle_moveEvent(self, event: pygame.event.Event):
        if event.key in (pygame.K_z, pygame.K_w):
            self.player_ismoving = True
            self.player_dir = "up"
        elif event.key == pygame.K_s:
            self.player_ismoving = True
            self.player_dir = "down"
        elif event.key in (pygame.K_q, pygame.K_a):
            self.player_ismoving = True
            self.player_dir = "left"
        elif event.key == pygame.K_d:
            self.player_ismoving = True
            self.player_dir = "right"

    def execute_move(self):
        if self.player_ismoving:
            if self.player_move_frame == 0:
                self.player.change_state("animated")
                self.player.rotate(self.player_dir)
                if self.player_dir == "up":
                    self.move_object(self.player, (0, -1))
                elif self.player_dir == "down":
                    self.move_object(self.player, (0, 1))
                elif self.player_dir == "left":
                    self.move_object(self.player, (-1, 0))
                elif self.player_dir == "right":
                    self.move_object(self.player, (1, 0))
            self.player_move_frame = (self.player_move_frame + 1) % 3
        else:
            self.player.change_state("fixed")

    def move_object(self, object: Player, pos_moves: tuple[int, int]):
        new_pos = (object.positions[0] + pos_moves[0], object.positions[1] + pos_moves[1])

        map_size = self.map.get_size()
        if new_pos[0] < 0 or new_pos[0] > map_size[0] or new_pos[1] < 0 or new_pos[1] > map_size[1]:
            return
        if self.map.get_at(new_pos) in ConfigAndStates.MAP_TILES_COLLISION:
            return
        
        self.player_has_moved = True

        object.update_position(new_pos)

    def can_wild_battle(self):
        if self.player_has_moved:
            if self.map.get_layer_at(self.player.positions) in ConfigAndStates.MAP_TILES_WILD_ENCOUNTER:
                if random() <= 0.1:
                    self.game.current_sys_state = ConfigAndStates.InstanceState.IN_WILD_BATTLE
                    self.player_has_moved = False

    def handle_events_in_wild_battle(self) -> ConfigAndStates.GameState:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = ConfigAndStates.GameState.ENDED
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = ConfigAndStates.GameState.ENDED
        except:
            self.gamestate = ConfigAndStates.GameState.CRASHED
        return self.gamestate

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
    def __init__(self, screen: pygame.Surface, CLOCK: pygame.time.Clock):
        self.screen: pygame.Surface = screen
        self.objects_map: SUPPORTED_OBJECTS = []
        self.gamestate = ConfigAndStates.GameState.NONE
        self.map: Map = None
        self.camera = Camera(0,0)
        self.CLOCK = CLOCK
        self.current_sys_state = ConfigAndStates.InstanceState.NONE
        self.menu = Menu(self)
        self.menu.set_up()
        self.set_up("01")
    
    def set_up(self, map_name:str):
        map_loaded = Map(map_name)
        self.map = map_loaded

        player = Player(1, 1)
        self.player = player

        self.objects_map.extend([self.map, self.player])

        self.gamestate = ConfigAndStates.GameState.RUNNING
        self.renderer = Renderer(self.screen, self.player, self.map, self.camera, self.objects_map, self.gamestate)
        self.current_sys_state = ConfigAndStates.InstanceState.MENU
        self.event_handler = EventsHandler(self.player, self.map, self.camera, self.objects_map, self.gamestate, self)

    def clean(self, screen: pygame.Surface, CLOCK: pygame.time.Clock):
        self.screen: pygame.Surface = screen
        self.objects_map: SUPPORTED_OBJECTS = []
        self.gamestate = ConfigAndStates.GameState.NONE
        self.map: Map = None
        self.camera = Camera(0,0)
        self.CLOCK = CLOCK
        self.current_sys_state = ConfigAndStates.InstanceState.NONE

    def start(self):
        while self.gamestate == ConfigAndStates.GameState.RUNNING:
            self.CLOCK.tick(ConfigAndStates.FTPS)
            self.update_loop()
            if self.gamestate == ConfigAndStates.GameState.RUNNING:
                self.render_loop()
        return

    def update_loop(self):
        if self.current_sys_state == ConfigAndStates.InstanceState.MENU:
            self.gamestate = self.menu.update()
        elif self.current_sys_state == ConfigAndStates.InstanceState.ON_MAP:
            self.gamestate = self.event_handler.handle_events_on_map()
        elif self.current_sys_state == ConfigAndStates.InstanceState.IN_WILD_BATTLE:
            self.gamestate = self.event_handler.handle_events_in_wild_battle()
        return
    
    def render_loop(self):
        if self.current_sys_state == ConfigAndStates.InstanceState.MENU:
            self.screen.fill(ConfigAndStates.LIGHT_GREY)
            self.menu.render(self.screen)
        elif self.current_sys_state == ConfigAndStates.InstanceState.ON_MAP:
            self.screen.fill(ConfigAndStates.BLACK)
            self.gamestate = self.renderer.render_on_map()
        elif self.current_sys_state == ConfigAndStates.InstanceState.IN_WILD_BATTLE:
            self.screen.fill(ConfigAndStates.LIGHT_GREY)
        pygame.display.flip()
        return

MENU_IMAGE = {
    "press_enter": pygame.image.load('assets/imgs/menu/enter_press.png').convert_alpha()
}

class Menu(RenderedComponent):
    def __init__(self, game: Game):
        super().__init__()
        self.game = game
    
    def set_up(self):
        pass

    def update(self) -> ConfigAndStates.GameState:
        try:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return ConfigAndStates.GameState.ENDED
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return ConfigAndStates.GameState.ENDED
                        elif event.key == pygame.K_RETURN:
                            self.game.current_sys_state = ConfigAndStates.InstanceState.ON_MAP
            return ConfigAndStates.GameState.RUNNING
        except:
            return ConfigAndStates.GameState.CRASHED
    
    def render(self, screen: pygame.Surface):
        try:
            rect = pygame.Rect(180, 11, 300, 75)
            screen.blit(MENU_IMAGE["press_enter"], rect)
            return RenderSucces()
        except:
            return 
