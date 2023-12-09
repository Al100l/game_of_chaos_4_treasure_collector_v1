import pygame
import math 
from game_settings import *
from class_Player import Player
from map_levels import world_map
from ray_casting import ray_casting_3d_optimize
from ray_casting import ray_casting_2d
from class_Drawing import Drawing

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_map = pygame.Surface((SCREEN_WIDTH // MAP_SCALE, SCREEN_HEIGHT//MAP_SCALE))


clock = pygame.time.Clock()


Renion = Player()

drawing = Drawing(screen, screen_map)

screen.fill(BLACK)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit()
            
        screen.fill(BLACK)
        Renion.movement()
        
        #2d
        ray_casting_2d(screen, Renion.position, Renion.angle)

        
        #3d
        '''
        pygame.draw.rect(screen, BLUE, (0, 0, SCREEN_WIDTH, SCREEN_HALF_HEIGHT))
        pygame.draw.rect(screen, PURPLE, (0, SCREEN_HALF_HEIGHT , SCREEN_WIDTH, SCREEN_HALF_HEIGHT))
        ray_casting_3d_optimize(screen, Renion.position, Renion.angle)
        #'''
        

        
        drawing.fps_drawing(clock)

        pygame.display.flip()
        clock.tick(FPS)
