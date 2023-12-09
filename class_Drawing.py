import pygame
from game_settings import *

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
    def fps_drawing(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, WHITE)
        self.sc.blit(render, FPS_POSITION)
    def player_movement_drawing():
        pass
 
