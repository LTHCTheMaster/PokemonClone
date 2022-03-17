import pygame
from camera import Camera
from map import Map
from player import Player
from gamestate import GameState
import configuration

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.objects: list = []
        self.gamestate = GameState.NONE
        self.map: Map = None
        self.camera = Camera(0,0)
        self.set_up()
    
    def set_up(self):
        map_loaded = Map("01")
        self.map = map_loaded

        player = Player(1, 1)
        self.player = player

        self.gamestate = GameState.RUNNING

    def update(self):
        self.screen.fill(configuration.BLACK)
        self.handle_events()
        self.camera.determine_camera(self.map, self.player)
        cam_pos = self.camera.get_pos()
        self.map.render(self.screen, cam_pos[0], cam_pos[1])
        self.player.render(self.screen, cam_pos[0], cam_pos[1])
        for object in self.objects:
            object.render(self.screen)
    
    def move_object(self, object: Player, pos_moves: list[int]):
        new_pos = [object.positions[0] + pos_moves[0], object.positions[1] + pos_moves[1]]

        map_size = self.map.get_size()
        if new_pos[0] < 0 or new_pos[0] > map_size[0] or new_pos[1] < 0 or new_pos[1] > map_size[1]:
            return
        if self.map.get_at(new_pos) == "W":
            return
        
        object.update_position(pos_moves)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gamestate = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gamestate = GameState.ENDED
                elif event.key in (pygame.K_z, pygame.K_w):
                    self.move_object(self.player, [0, -1])
                elif event.key == pygame.K_s:
                    self.move_object(self.player, [0, 1])
                elif event.key in (pygame.K_q, pygame.K_a):
                    self.move_object(self.player, [-1, 0])
                elif event.key == pygame.K_d:
                    self.move_object(self.player, [1, 0])
