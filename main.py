import pygame
import numpy as np
import math
import time


#import game_settings
#from class_Hero import Hero
#from class_Drawing import Drawing
#from level_maps import *

#game settings

SCREEN_WIDTH        =   1200
SCREEN_HEIGHT       =   800
SCREEN_HALF_WIDTH   =   SCREEN_WIDTH   // 2
SCREEN_HALF_HEIGHT  =   SCREEN_HEIGHT  // 2

map_width = SCREEN_WIDTH // 25
map_height = SCREEN_HEIGHT // 25

#player settings
last_player_position = player_position = (17, 22)


player_speed = 5

player_angle = 0

FIELD_OF_VIEW = math.pi / 3

HALF_FIELD_OF_VIEW =FIELD_OF_VIEW /2

NUM_RAYS_IN_FIELD_OF_VIEW = 120

DELTA_ANGLE = FIELD_OF_VIEW / NUM_RAYS_IN_FIELD_OF_VIEW

MAX_DEPTH = 200

FPS = 40
#map

TILE = SCREEN_HEIGHT // map_height
#TILE = 60

#mini map

MAP_SCALE = 5

MAP_TILE = TILE // MAP_SCALE

MAP_POSITION = (0, SCREEN_HEIGHT - SCREEN_HEIGHT // MAP_SCALE)
#colors

BLACK   = (0,0,0)

DARKGRAY = (110,110,110)

WHITE   = (255,255,255)

RED     = (220,0,0)

ORANGE  = (180,140,0)

YELLOW  = (0,120,120)

GREEN   = (0,220,0)

DARK_GREEN = (54, 109, 9)

BLUE    = (0,0,220)

PURPLE  = (120,0,120)



#ray_casting

SCALE = SCREEN_WIDTH // NUM_RAYS_IN_FIELD_OF_VIEW


# FPS settings

FPS_POSITION =(SCREEN_WIDTH - 65, 5)

class Cards:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

class Hero:

    def __init__(self, name, healthpoints, damage, armor, attack_range, movement_speed, vision_distance, player_pos):
        self.name = name
        self.x, self.y = player_pos
        self.healthpoints = healthpoints
        self.damage = damage
        self.armor = armor
        self.attack_range = attack_range
        self.movement_speed = movement_speed
        self.vision_distance = vision_distance

    def movement(self,current_map):
        #print("begin", self.x, self.y)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # north
            if current_map[self.x-1][self.y]!=1:
                self.x += -1
                self.y += 0


        elif keys[pygame.K_s]:  # south
            if current_map[self.x + 1][self.y] != 1:
                self.x += 1
                self.y += 0

        elif keys[pygame.K_a]:  # west
            if current_map[self.x ][self.y-1] != 1:
                self.x += 0
                self.y += -1

        elif keys[pygame.K_d]:  # east
            if current_map[self.x][self.y+1] != 1:
                self.x += 0
                self.y += 1
        #print(self.x, self.y)
    def fight(self, any_NPC_position):
        #if (player_position[0] + 1 == any_NPC_position[0]) or (player_position[0] - 1 == any_NPC_position[0]) or (player_position[0] + 1 == any_NPC_position[0]) or (player_position[0] - 1 == any_NPC_position[0]):
            #all NPC that are in surrounding square take damage
            pass
    def take(self, any_gold_position):
        #if (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]) or (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]):
            # all gold and medallions that are in surrounding square puts into backpack
            pass

    @property
    def position(self):
        return (self.x, self.y)

    def print_all_characteristics(self):
        print("name: ", self.name,
              "healthpoints: ", self.healthpoints,
              "damage: ", self.damage,
              "armor : ", self.armor,
              "attack_range: ", self.attack_range,
              "movement_speed: ", self.movement_speed,
              "vision_distance: ", self.vision_distance,
              "location: ", (self.x, self.y))


class Button:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.SysFont(None, 40)
        self.width, self.height = 200, 70
        self.position = pygame.Rect(position, (self.width, self.height))
        self.is_hovered = False

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN if self.is_hovered else DARK_GREEN, self.position)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.position.center)
        screen.blit(text_surface, text_rect)
    def check_click(self, pos):
        if self.position.collidepoint(pos):
            return True
        return False



class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
    def fps_drawing(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, YELLOW)
        self.sc.blit(render, FPS_POSITION)


    def draw_walls(self,sc, cur_map):
        for x, y in cur_map:
            pygame.draw.rect(sc, RED, (x, y, TILE, TILE), TILE)

    def draw_player(self, sc, player_pos, cur_player_pos):
        x, y = player_pos
        for x, y in cur_player_pos:
            pygame.draw.circle(sc, GREEN, (x+TILE//2, y+TILE//2), TILE//2)
    def draw_player_vision(self, sc, cur_player_vis_map):
        for x, y in cur_player_vis_map:
            pygame.draw.rect(sc,BLACK, (x, y, TILE, TILE), TILE)
    def draw_decor(self,sc,cur_dec_map):
        pass

def print_text( message, x, y, font_color):
    font_type = pygame.font.SysFont(None, 25)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
def generate_training_level_layers (map_width, map_height, vis_distance):


    # player_pos
    #слой с отображением позиции игрока
    matrix_player_pos_map = np.zeros((map_height,map_width))
    matrix_player_pos_map[player_position] = 1
    last_player_position = player_position
    #print(matrix_player_pos_map, '\n')

    # создаём стек используемых для прорисовки позиции игрока точек
    cur_player_pos_on_map = matrix_player_pos_map
    cur_player_map = set()
    for j, row in enumerate(cur_player_pos_on_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_map.add((i * TILE, j * TILE))

    #wal
    #слой с изображением стен
    #matrix_wal_map = np.ones((map_height,map_width))
    #внешняяя стена вокруг
    #matrix_wal_map[1:-1,1:-1:] = 0
    #внутренние стены
    #matrix_wal_map[5:-5,5:-5:] = 1
    matrix_wal_map =[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 9, 9, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 9, 9, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    ]
    #print(matrix_wal_map, '\n')
    #создаём стек используемых для прорисовки квадратиков стен точек
    cur_matrix_wal_map = matrix_wal_map
    cur_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_map.add((i*TILE, j*TILE))

    #vis
    #создаём слой видимости игроком
    # слой с отображением позиции игрока
    matrix_player_vis_map = np.ones((map_height, map_width))

    matrix_player_vis_map[(player_position[0] - vis_distance):(player_position[0] + vis_distance+1),
                            (player_position[1] - vis_distance): (player_position[1] + vis_distance+1):] = 0
    matrix_player_vis_map[(player_position[0] - 1):(player_position[0] + 1 + 1),
    (player_position[1] - 1): (player_position[1] + 1 + 1):] = 0
    matrix_player_vis_map[(player_position[0] - 2):(player_position[0] + 2 + 1),
    (player_position[1] - 2): (player_position[1] + 2 + 1):] = 0
    last_player_position = player_position
    # print(matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки зрения игрока точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))

    # dec
    # создаём наполнение/декор



    return(cur_map,
           cur_player_map,
           cur_player_vis_map,
           matrix_player_pos_map,
           matrix_wal_map,
           matrix_player_vis_map)

def change_player_position(last_player_pos, player_position, matrix_walls_map, matrix_player_vision_map, vis_distance):

    # player_pos
    # слой с отображением позиции игрока
    matrix_player_pos_map = np.zeros((map_height, map_width))
    matrix_player_pos_map[last_player_pos] = 0
    matrix_player_pos_map[player_position] = 1
    last_player_pos = player_position
    # print(matrix_player_pos_map, '\n')
    # создаём стек используемых для прорисовки точек
    cur_player_pos_on_map = matrix_player_pos_map
    cur_player_map = set()
    for j, row in enumerate(cur_player_pos_on_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_map.add((i * TILE, j * TILE))

    # wal
    # слой с изображением стен
    #matrix_wal_map = np.ones((map_height, map_width))
    # внешняяя стена вокруг
    #matrix_wal_map[1:-1, 1:-1:] = 0
    # внутренние стены
    #matrix_wal_map[5:-5, 5:-5:] = 1
    # print(matrix_wal_map, '\n')
    # создаём стек используемых для прорисовки квадратиков стен точек
    matrix_wal_map = matrix_walls_map
    cur_matrix_wal_map = matrix_wal_map
    cur_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_map.add((i * TILE, j * TILE))

    #vis
    # слой с отображением зрения игрока
    #используем основную матрицу
    matrix_player_vis_map = matrix_player_vision_map

    matrix_player_vis_map[(player_position[0] - vis_distance):(player_position[0]+vis_distance+1),
                          (player_position[1] - vis_distance): (player_position[1] + vis_distance+1):] = 0
    matrix_player_vis_map[(player_position[0] - 1):(player_position[0] + 1 + 1),
    (player_position[1] - 1): (player_position[1] + 1 + 1):] = 0
    matrix_player_vis_map[(player_position[0] - 2):(player_position[0] + 2 + 1),
    (player_position[1] - 2): (player_position[1] + 2 + 1):] = 0
    #print(matrix_player_vis_map)
    last_player_pos = player_position
    #print(matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))

    return (cur_map, cur_player_map, cur_player_vis_map, matrix_player_pos_map, matrix_wal_map, matrix_player_vis_map)

def pause():
    #pygame.display.set_mode((640,480))
    pygame.display.set_caption('Pause')
    screen.fill(BLACK)
    print_text("Paused", 400, 100, font_color =WHITE)
    print_text("для выхода из паузы нажмите Escape", 400, 150, font_color =WHITE)

    pygame.display.flip()
    paused = True
    while paused:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                paused = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                paused = False

    pygame.display.set_caption('First level')
    pygame.display.update()

pygame.init()

background_image_to_start_screen = pygame.image.load("ctulkhu.jpg")
background_image_to_name_input = pygame.image.load("nemeron_gates.jpg")
background_image_to_training_level_v1 = pygame.image.load("background_for_training_level_v2.jpg")
background_image_to_name_input = pygame.image.load("nemeron_gates.jpg")
background_image_to_lor = pygame.image.load("page2.jpg")
#screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_map = pygame.Surface((SCREEN_WIDTH // MAP_SCALE, SCREEN_HEIGHT//MAP_SCALE))

pygame.display.set_caption('Начальный экран')

drawing = Drawing(screen, screen_map)

# создание кнопок
start_button = Button("Начать игру", (460, 560))
start_button.width, start_button.height = 400 ,100
start_button.position = pygame.Rect((380, 560), (start_button.width, start_button.height))
menu_button = Button("Меню", (500, 680))

back_button2 = Button("Назад", (50, 700))
next_button = Button("Далее", (950, 700))

settings_button = Button("Настройки", (700, 700))
about_button = Button("Об авторах", (300, 700))
back_button = Button("На начальный экран", (50, 700))
back_button.font = pygame.font.SysFont(None, 20)
exit_button = Button("Выйти", (950, 700))


back_exit_button = Button("Остаться", (300, 660))
real_exit_button = Button("Выйти", (700, 660))

current_screen = "main"

# основной цикл приложения
running = True

screen.blit(background_image_to_start_screen, (0, 0))
while running:
    screen.blit(background_image_to_start_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            menu_button.is_hovered = menu_button.position.collidepoint(pos)
            settings_button.is_hovered = settings_button.position.collidepoint(pos)
            exit_button.is_hovered = exit_button.position.collidepoint(pos)
            start_button.is_hovered = start_button.position.collidepoint(pos)
            back_button.is_hovered = back_button.position.collidepoint(pos)
            back_button2.is_hovered = back_button2.position.collidepoint(pos)
            next_button.is_hovered = next_button.position.collidepoint(pos)
            about_button.is_hovered = about_button.position.collidepoint(pos)
            back_exit_button.is_hovered = back_exit_button.position.collidepoint(pos)
            real_exit_button.is_hovered = real_exit_button.position.collidepoint(pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_screen == "main":
                if start_button.check_click(event.pos):
                    current_screen = "naming"
                    pygame.display.set_caption('Об игре')
                    screen.blit(background_image_to_lor, (0, 0))
                elif menu_button.check_click(event.pos):
                    current_screen = "menu"
            elif current_screen == "menu":
                if back_button.check_click(event.pos):
                    current_screen = "main"
                elif exit_button.check_click(event.pos):
                    current_screen = "exit"
                elif settings_button.check_click(event.pos):
                    print("Открыть окно настроек")
                elif about_button.check_click(event.pos):
                    print("трек о вас, о нас")
            elif current_screen == "naming":
                if back_button2.check_click(event.pos):
                    current_screen = "main"
                elif next_button.check_click(event.pos):
                    current_screen = "training"
            elif current_screen == "exit":
                if back_exit_button.check_click(event.pos):
                    current_screen = "menu"
                elif real_exit_button.check_click(event.pos):
                    running = False


    if current_screen == "main":
        start_button.draw(screen)
        menu_button.draw(screen)
    elif current_screen == "menu":
        back_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
        about_button.draw(screen)
    elif current_screen == "exit":
        print_text("Вы уверены что хотите выйти из игры?",300, 300)
        back_exit_button.draw(screen)
        real_exit_button.draw(screen)
    elif current_screen == "naming":
        font = pygame.font.SysFont("Gabriola", 25)
        #'''
        text_introduction =["Приветствую тебя, путник!",
                            " ",
                            "В многолетних воинах был истреблён народ арисшеев.",
                            "Всё, что осталось от разумных, поклонявшихся богу Смерти - это величественные могильники, ",
                            "простирающиеся на тысячи километров под землёй победителей.",
                            " ",
                            "Смельчаки. называющие себя искателями, отваживаются спускаться в скепы мертвого народа, ",
                            " ",
                            "а везунчики ещё и возвращаться с уникальной добычей",
                            " ",
                            "Подземные гробницы аритшеев полны ловушек и опасностей, "
                            "орды нежити и мертвецов поджидают в лабиринтах темных коридоров тех, ",
                            "кто отважится туда спуститься. ",
                            "Армии воинов, даже после своей смерти хранящих покой своих владык"]
        movement = 0
        for i in text_introduction:
            text_surf_1 = font.render(i, True, WHITE)
            screen.blit(text_surf_1, (50, 400+movement))
            movement+=20
        #'''
        '''
        text = "Введите имя вашего персонажа"
        font = pygame.font.SysFont(None, 50)
        text_surf_2 = font.render(text, True, WHITE)
        screen.blit(text_surf_2, (400, 600))
        '''
        back_button2.draw(screen)
        next_button.draw(screen)
    elif current_screen == "training":
        pygame.display.set_caption('Обучение')
        break
    pygame.display.flip()




#print(screen)
clock = pygame.time.Clock()

#players_nick = input("Введите имя вашего персонажа: ")
players_nick = "Ренион"

Player = Hero(  name           = players_nick,
                player_pos     = player_position,
                healthpoints   = 25,
                damage         = 1,
                armor          = 0,
                attack_range   = 1,
                movement_speed = 1,
                vision_distance= 3)




(current_map,
 current_player_map,
 current_player_vision_map,
 matrix_player_position_map,
 matrix_walls_map,
 matrix_player_vision_map)  =  generate_training_level_layers(map_width =  map_width, map_height = map_height, vis_distance = Player.vision_distance )
screen.fill(BLACK)


running_training   = True


running_W_training = True
running_S_training = False
running_A_training = False
running_D_training = False
running_P_training = False
running_F_training = False
running_T_training = False
running_M_training = False
running_B_training = False
running_E_training = False
running_C_training = False


stop_training      = False


while running_training:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            # quests
            pass
        '''
        elif keys[pygame.K_h]:
            #hide
            pass
        '''
        screen.fill(BLACK)
        screen.blit(background_image_to_training_level_v1, (0, 0))
        (current_map,
         current_player_map,
         current_player_vision_map,
         matrix_player_position_map,
         matrix_walls_map,
         matrix_player_vision_map) = change_player_position(last_player_pos=last_player_position,
                                                            player_position=player_position,
                                                            matrix_walls_map=matrix_walls_map,
                                                            matrix_player_vision_map=matrix_player_vision_map,
                                                            vis_distance=Player.vision_distance)

        # drawing.draw_walls(sc= screen, cur_map = current_map)
        drawing.draw_player(sc=screen,
                            player_pos=player_position,
                            cur_player_pos=current_player_map)
        drawing.draw_player_vision(sc=screen, cur_player_vis_map=current_player_vision_map)
        drawing.fps_drawing(clock)
        Player.movement(matrix_walls_map)
        player_position = (Player.x, Player.y)


        if (running_W_training== 1):
            print_text(message = "Чтобы двинуться вперёд, нажмите W", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_w]:
                running_W_training = False
                running_S_training = True
                pass
        if (running_S_training== 1):
            print_text(message ="Чтобы двинуться назад, нажмите S", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_s]:
                running_S_training = False
                running_A_training = True
                pass
        if (running_A_training == 1):
            print_text(message ="Чтобы двинуться влево, нажмите A", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_a]:
                running_A_training = False
                running_D_training = True
                pass
        if (running_D_training == 1):
            print_text(message ="Чтобы двинуться вправо, нажмите D", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_d]:
                running_D_training = False
                running_P_training = True
                pass
        if (running_P_training == 1):
            print_text(message ="Чтобы остановить игру, нажмите P", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_p]:
                pause()
                running_P_training = False
                running_F_training = True

                pass
        if (running_F_training == 1):
            print_text(message ="Ударить стоящего рядо врага, нажмите F", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_f]:
                running_F_training = False
                running_T_training = True

                pass
        if (running_T_training == 1):
            print_text(message ="Чтобы взять предмет, нажмите  T", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_t]:
                running_T_training = False
                running_M_training = True
                pass
        if (running_M_training == 1):
            print_text(message ="Чтобы открыть меню, нажмите  M", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_m]:
                running_M_training = False
                running_B_training = True
                pass
        if (running_B_training == 1):
            print_text(message ="Чтобы открыть книгу заклинаний, нажмите  B", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_b]:
                running_B_training = False
                running_E_training = True
                pass
        if (running_E_training == 1):
            print_text(message ="Чтобы открыть инвентарь, нажмите  E", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_e]:
                running_E_training = False
                running_C_training = True
                pass
        if (running_C_training == 1):
            print_text(message ="Чтобы открыть активатор, нажмите  C", x=50, y=400, font_color=WHITE)
            if keys[pygame.K_c]:
                running_C_training = False
                running_training = True
                pass

        if (stop_training == False):
            print_text(message ="Чтобы завершить обучение. нажмите Backspace", x=400 , y=10, font_color=WHITE)
            if keys[pygame.K_BACKSPACE]:
                running_training = False

        time.sleep(0.01)
        pygame.display.flip()
        clock.tick(FPS)



pygame.display.set_caption('first level')
running_first_level = True
while running_first_level:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            #pause
            pass
        elif keys[pygame.K_q]:
            #quests
            pass
        elif keys[pygame.K_m]:
            #menu
            pass
        elif keys[pygame.K_b]:
            #book_with_cards
            pass
        elif keys[pygame.K_e]:
            #equipment
            pass
        elif keys[pygame.K_t]:
            #take
            pass
        elif keys[pygame.K_f]:
            #fight
            pass
        elif keys[pygame.K_c]:
            #cards Активатор
            pass
        '''
        elif keys[pygame.K_h]:
            #hide
            pass
        '''

        screen.fill(BLACK)
        screen.blit(background_image_to_training_level_v1, (0, 0))
        (current_map,
         current_player_map,
         current_player_vision_map,
         matrix_player_position_map,
         matrix_walls_map,
         matrix_player_vision_map) = change_player_position(last_player_pos=last_player_position,
                                                            player_position = player_position,
                                                            matrix_walls_map = matrix_walls_map,
                                                            matrix_player_vision_map = matrix_player_vision_map,
                                                            vis_distance = Player.vision_distance)
        
        #drawing.draw_walls(sc= screen, cur_map = current_map)
        drawing.draw_player(sc= screen, 
                            player_pos=player_position, 
                            cur_player_pos=current_player_map)
        drawing.draw_player_vision( sc= screen, cur_player_vis_map=current_player_vision_map)
        drawing.fps_drawing(clock)
        
        Player.movement(matrix_walls_map)
        player_position = (Player.x, Player.y)

        time.sleep(0.01)
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()