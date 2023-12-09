import pygame
from game_settings import *
from map_levels import world_map
import math

def ray_casting_2d(sc, player_position, player_angle):
    current_angle = player_angle - HALF_FIELD_OF_VIEW
    x_0, y_0 = player_position
    for ray in range(NUM_RAYS_IN_FIELD_OF_VIEW):
        sin_a =  math.sin(current_angle)
        cos_a =  math.cos(current_angle)
        for depth in range(MAX_DEPTH):
            x = x_0 + depth * cos_a
            y = y_0 + depth * sin_a
            pygame.draw.line(sc, DARKGRAY, player_position, (x, y), 2)
            if (x// TILE * TILE, y // TILE* TILE) in world_map:
                break
        current_angle += DELTA_ANGLE

    
        ''' Направление взгляда игрока '''
        #
        #'''
        pygame.draw.line(sc,
                         GREEN,
                         player_position,
                        (x_0  + SCREEN_WIDTH * math.cos(player_angle),
                        y_0  + SCREEN_WIDTH * math.sin(player_angle)),
                         )
        #'''
        #
        #'''Отрисовка карты вид сверху'''
        #
        #'''
        pygame.draw.circle(sc, GREEN, player_position, 12) #Рисуем игрока сверху
        
        for x, y in world_map:
            pygame.draw.rect(sc, DARK_GREEN, (x, y, TILE, TILE), 8 )
        #'''
        #




def ray_casting_3d (sc, player_position, player_angle):
    current_angle = player_angle - HALF_FIELD_OF_VIEW
    x_0, y_0 = player_position
    for ray in range(NUM_RAYS_IN_FIELD_OF_VIEW):
        sin_a =  math.sin(current_angle)
        cos_a =  math.cos(current_angle)
        for depth in range(MAX_DEPTH):
            x = x_0 + depth * cos_a
            y = y_0 + depth * sin_a
            if (x// TILE * TILE, y // TILE* TILE) in world_map:
                #исправляем эффект рыбьего глаза
                depth *= math.cos(player_angle - current_angle)
                #
                proj_wall_height = PROJECT_COEFFICIENT / depth
                #затемнение с растоянием
                c = 255 / (1 +depth*depth*0.0001)
                color = (c, c, c)
                #
                pygame.draw.rect(sc,
                                 color,
                                 (ray * SCALE,
                                  SCREEN_HALF_HEIGHT - proj_wall_height // 2,
                                  SCALE,
                                  proj_wall_height)
                                 )
                
                break
        current_angle += DELTA_ANGLE





        
def mapping(a, b):
    return (a//TILE) * TILE, (b//TILE) * TILE

def ray_casting_3d_optimize (sc, player_position, player_angle):
    O_x, O_y = player_position
    x_m, y_m = mapping(O_x, O_y)
    current_angle = player_angle - HALF_FIELD_OF_VIEW
    for ray in range(NUM_RAYS_IN_FIELD_OF_VIEW):
        sin_a =  math.sin(current_angle)
        cos_a =  math.cos(current_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        #"""Оптимизация записи""" x, dx =(x_m +TILE, 1)if cos_a >=0 else(x_m,-1)
        if cos_a>= 0:
            x = x_m + TILE
            dx = 1
        else:
            x = x_m
            dx = -1
        for i in range(0, SCREEN_WIDTH, TILE):
            depth_vertical = (x - O_x)/ cos_a
            y = O_y +depth_vertical *sin_a
            if mapping(x + dx, y) in world_map:
                break
            x+= dx*TILE
        #    
        #
        #
        
        if sin_a >=0 :
            y, dy = y_m +TILE , 1 
        else:
            y, dy = y_m, -1

        for i in range(0, SCREEN_HEIGHT, TILE):
            depth_horizontal = (y - O_y)/ sin_a
            x = O_x + depth_horizontal * cos_a
            if mapping( x, y+dy ) in world_map:
                break
            y += dy* TILE

        depth = min (depth_vertical, depth_horizontal)
        #исправляем эффект рыбьего глаза
        depth *= math.cos(player_angle - current_angle)
        #
        proj_wall_height = PROJECT_COEFFICIENT / depth
        #затемнение с растоянием
        c = 255 / (1 + depth*depth*0.0001)
        color = (c, c//2, c//3)
        #
        pygame.draw.rect(sc,
                        color,
                        (ray * SCALE,
                        SCREEN_HALF_HEIGHT - proj_wall_height // 2,
                        SCALE,
                        proj_wall_height)
                        )
        current_angle += DELTA_ANGLE




        
