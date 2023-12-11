import pygame
import numpy as np
import math
import time

pygame.init()

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
last_player_position = (17, 22)
player_position = (17, 22)


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

GREENS=(176, 212, 144)

DARK_GREEN = (54, 109, 9)

BLUE    = (0,0,220)

PURPLE  = (120,0,120)

DARK_BLUE =(34, 93, 92)
#maps

matrix_walls_map =[
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

#ray_casting

SCALE = SCREEN_WIDTH // NUM_RAYS_IN_FIELD_OF_VIEW


# FPS settings

FPS_POSITION =(SCREEN_WIDTH - 65, 5)


class Magic_book:
    pass
class Cards:
    def __init__(self, card_name, discription,number, image, card_form):
        self.card_name = card_name
        self.discription = discription
        self.active = 1
        self.number = number
        self.image = image
        self.card_form = card_form
    '''
    def move_to_activator(self):
        pass
    def move_to_book(self):
        pass
    '''
    def activate(self):
        self.active = 0
        pass
    def print_card(self):
        print(self.card_name)
        print(self.number)

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
        pygame.draw.rect(screen, GREENS if self.is_hovered else DARK_BLUE, self.position)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.position.center)
        screen.blit(text_surface, text_rect)
    def check_click(self, pos):
        if self.position.collidepoint(pos):
            return True
        return False


# создание кнопок
start_button = Button("Начать игру", (460, 560))
start_button.width, start_button.height = 400 ,100
start_button.position = pygame.Rect((380, 560), (start_button.width, start_button.height))
menu_button = Button("Меню", (480, 680))
menu_button.width, menu_button.height = 200 ,80
menu_button.position = pygame.Rect((480, 680), (menu_button.width, menu_button.height))

back_button2 = Button("Назад", (50, 700))
next_button = Button("Далее", (950, 700))

back_button = Button("На начальный экран", (40, 700))
back_button.font = pygame.font.SysFont(None, 20)
about_button = Button("Об авторах", (260, 700))
back_button3 = Button("К игре", (500, 700))
settings_button = Button("Настройки", (720, 700))
exit_button = Button("Выйти", (940, 700))


back_exit_button = Button("Остаться", (300, 660))
real_exit_button = Button("Выйти", (700, 660))

magic_book_button   = Button("Книга заклинаний", (500, 200))
quests_button       = Button("Квесты", (500, 300))
equipment_button    = Button("Инвентарь", (500, 400))
exit_button_2       = Button("Выйти", (500, 700))

activate_card_button_1 = Button("Активировать", (50, 50))
activate_card_button_2 = Button("Активировать", (50, 150))
activate_card_button_3 = Button("Активировать", (50, 250))
activate_card_button_4 = Button("Активировать", (50, 350))
activate_card_button_5 = Button("Активировать", (50, 450))
activate_card_button_6 = Button("Активировать", (750, 50))
activate_card_button_7 = Button("Активировать", (750, 150))
activate_card_button_8 = Button("Активировать", (750, 250))
activate_card_button_9 = Button("Активировать", (750, 350))
activate_card_button_10 = Button("Активировать", (750, 450))
#activate_card_button_ = Button("Активировать", (50, 50))
#activate_card_button_ = Button("Активировать", (50, 50))

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
    def draw_rect(self, screen):
        # Отрисовка фона статус бара
        pygame.draw.rect(screen, color=(220,220,220),rect=(0,0,1200,800))
class StatusBar:
    def __init__(self, x, y, width, height, min_value, max_value, current_value, text, color= (200, 200, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value
        self.text = text
        self.color = color
    def draw(self, screen):
        # Отрисовка фона статус бара
        pygame.draw.rect(screen, color=(220,220,220),rect=(self.x, self.y, self.width, self.height))

        # Рассчитываем ширину ползунка в зависимости от значений
        range = self.max_value - self.min_value
        value_offset = self.current_value - self.min_value
        slider_width = int((value_offset / range) * self.width)

        # Отрисовываем ползунок статус бара
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, slider_width, self.height))

        # Отрисовка текста
        print_text(message=self.text, x = self.x, y = self.y, font_color = WHITE)
    def update_value(self, new_value):
        # Обновляем текущее значение статус бара
        self.current_value = new_value
def print_text( message, x, y, font_color, size = 25):
    font_type = pygame.font.SysFont(None, size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
def training_level_layers_generate (map_width, map_height, vis_distance):


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
def cards_initialization():
    mythryl_sword=Cards(                card_name ='Мифриловый меч',                discription="",     number = 1      ,image=""       ,card_form="")
    fog_lion=Cards(                     card_name ="Туманный лев",                  discription="",     number = 2      ,image=""       ,card_form="")
    grakula=Cards(                      card_name="Гракула",                        discription="",     number = 3      ,image=""       ,card_form="")
    sprigan=Cards(                      card_name="Сприган. мастер ловушек",        discription="",     number = 4      ,image=""       ,card_form="")
    crystal_mole=Cards(                 card_name="Кристаллический крот",           discription="",     number = 5      ,image=""       ,card_form="")
    kayrun_hammer=Cards(                card_name="Молот Кайруна",                  discription="",     number = 6      ,image=""       ,card_form="")
    wind_of_ice_debris=Cards(           card_name="Ветер ледяных осколков",         discription="",     number = 7      ,image=""       ,card_form="")
    breath_of_dragons_ancestors=Cards(  card_name="Дыхание прародителей драконов",  discription="",     number = 8      ,image=""       ,card_form="")
    giant_eye=Cards(                    card_name="Глаз исполина",                  discription="",     number = 9      ,image=""       ,card_form="")
    armor_of_rapid_strikes=Cards(       card_name="Доспех стремительных ударов",    discription="",     number =10      ,image=""       ,card_form="")
    '''
    =Cards(card_name="", discription="")
    '''
    all_cards = [   mythryl_sword,
                    fog_lion,
                    grakula,
                    sprigan,
                    crystal_mole,
                    kayrun_hammer,
                    wind_of_ice_debris,
                    breath_of_dragons_ancestors,
                    giant_eye,
                    armor_of_rapid_strikes]
    return(all_cards)
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

def generate_pause(current_screen):
    pygame.display.set_caption('Пауза')
    #current_screen = "pause"
    screen.fill(BLACK)
    pygame.display.flip()
    paused = True

    while paused:
        screen.blit(pygame.image.load("nemeron_gates.jpg"), (-100, 0))
        print_text("Для выхода из паузы нажмите Escape", 400, 150, font_color=WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                paused = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                magic_book_button.is_hovered =magic_book_button.position.collidepoint(pos)
                quests_button.is_hovered =quests_button.position.collidepoint(pos)
                equipment_button.is_hovered =equipment_button.position.collidepoint(pos)
                exit_button_2.is_hovered = exit_button_2.position.collidepoint(pos)
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "pause":
                    if magic_book_button.check_click(event.pos):
                        current_screen = "magic_book"
                    if quests_button.check_click(event.pos):
                        current_screen = "quests"
                    if equipment_button.check_click(event.pos):
                        current_screen = "equipment"
                    if exit_button_2.check_click(event.pos):
                        current_screen = "main"
                    elif back_button2.check_click(event.pos):
                        current_screen = "training"

        if current_screen == "pause":
            magic_book_button.draw(screen)
            quests_button.draw(screen)
            equipment_button.draw(screen)
            exit_button_2.draw(screen)
            back_button2.draw(screen)
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen = "training")
        elif current_screen == "magic_book":
            pygame.display.set_caption('Книга заклинаний')
            generate_magic_book(cards_compilation=all_cards, current_screen="magic_book")
        elif current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            generate_main(current_screen="main")
        elif current_screen == "equipment":
            pygame.display.set_caption('Инвентарь')
            generate_equipment(current_screen="equipment")
        pygame.display.flip()



    pygame.display.set_caption('First level')
    pygame.display.update()

def generate_menu(current_screen):
    pygame.display.set_caption('Меню')
    screen.blit(background_image_to_lor, (0, 0))
    running_menu = True
    while running_menu:
        '''
        screen.blit(pygame.image.load("nemeron_gates.jpg"), (-100, 0))
        print_text("Для выхода из меню нажмите Escape", 400, 150, font_color=WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                settings_button.is_hovered = settings_button.position.collidepoint(pos)
                exit_button.is_hovered = exit_button.position.collidepoint(pos)
                back_button.is_hovered = back_button.position.collidepoint(pos)
                back_button3.is_hovered = back_button3.position.collidepoint(pos)
                about_button.is_hovered = about_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "menu":
                    if back_button.check_click(event.pos):
                        current_screen = "main"
                    elif exit_button.check_click(event.pos):
                        current_screen = "exit"
                    elif back_button3.check_click(event.pos):
                        current_screen = "training"
                    elif settings_button.check_click(event.pos):
                        print("Открыть окно настроек")
                    elif about_button.check_click(event.pos):
                        print("трек о вас, о нас")

        if current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
            back_button3.draw(screen)
        elif current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            generate_main (current_screen="main")
        elif current_screen == "exit":
            pygame.display.set_caption('Выход')
            generate_exit(current_screen = "exit")
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen = "training")

        pygame.display.flip()
def generate_training(current_screen, player_position = player_position, last_player_position=last_player_position,matrix_walls_map=matrix_walls_map, matrix_player_vision_map=np.ones((map_height, map_width))):
    running_training = True

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

    stop_training = False
    current_screen = "training"
    while running_training:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running_training = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                generate_main(current_screen="quests")
            if keys[pygame.K_m]:

                current_screen = "menu"
                pygame.display.set_caption('Меню')
                generate_main(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                generate_magic_book(cards_compilation=all_cards, current_screen="magic_book")

            if keys[pygame.K_p]:
                generate_pause(current_screen="pause")

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

            if (running_W_training == 1):
                print_text(message="Чтобы двинуться вперёд, нажмите W", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_w]:
                    running_W_training = False
                    running_S_training = True
                    pass
            if (running_S_training == 1):
                print_text(message="Чтобы двинуться назад, нажмите S", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_s]:
                    running_S_training = False
                    running_A_training = True
                    pass
            if (running_A_training == 1):
                print_text(message="Чтобы двинуться влево, нажмите A", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_a]:
                    running_A_training = False
                    running_D_training = True
                    pass
            if (running_D_training == 1):
                print_text(message="Чтобы двинуться вправо, нажмите D", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_d]:
                    running_D_training = False
                    #running_F_training = True #comment after pause editing
                    running_P_training = True
                    pass
            #'''
            if (running_P_training == 1):
                print_text(message="Чтобы остановить игру, нажмите P", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_p]:
                    running_P_training = False
                    running_F_training = True
            #'''
            if (running_F_training == 1):
                print_text(message="Ударить стоящего рядо врага, нажмите F", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_f]:
                    running_F_training = False
                    running_T_training = True

                    pass
            if (running_T_training == 1):
                print_text(message="Чтобы взять предмет, нажмите  T", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_t]:
                    running_T_training = False
                    running_M_training = True
                    pass
            if (running_M_training == 1):
                print_text(message="Чтобы открыть меню, нажмите  M", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_m]:
                    running_M_training = False
                    running_B_training = True
                    pass
            if (running_B_training == 1):
                print_text(message="Чтобы открыть книгу заклинаний, нажмите  B", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_b]:
                    running_B_training = False
                    running_E_training = True
                    pygame.display.set_caption('Книга заклинаний')
                    current_screen = "magic_book"
                    pass
            if (running_E_training == 1):
                print_text(message="Чтобы открыть инвентарь, нажмите  E", x=50, y=400, font_color=WHITE)
                if keys[pygame.K_e]:
                    running_E_training = False
                    running_training = True
                    pygame.display.set_caption('Инвентарь')
                    current_screen = "equipment"
                    pass

            if (stop_training == False):
                print_text(message="Чтобы завершить обучение. нажмите Backspace", x=400, y=10, font_color=WHITE)
                if keys[pygame.K_BACKSPACE]:
                    generate_first_level()
                    running_training = False


        health_bar.draw(screen)
        damage_bar.draw(screen)
        vision_distance_bar.draw(screen)
        time.sleep(0.01)
        pygame.display.flip()
        clock.tick(FPS)


def generate_first_level(current_screen="first level", player_position = player_position, last_player_position=last_player_position,matrix_walls_map=matrix_walls_map, matrix_player_vision_map=np.ones((map_height, map_width))):
    pygame.display.set_caption('first level')
    running_first_level = True
    while running_first_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_training = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                generate_main(current_screen="quests")
            if keys[pygame.K_m]:

                current_screen = "menu"
                pygame.display.set_caption('Меню')
                generate_main(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                generate_magic_book(cards_compilation=all_cards, current_screen="magic_book")

            if keys[pygame.K_p]:
                generate_pause(current_screen="pause")

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

            health_bar.draw(screen)
            damage_bar.draw(screen)
            vision_distance_bar.draw(screen)
            time.sleep(0.01)
            pygame.display.flip()
            clock.tick(FPS)
def generate_magic_book(cards_compilation, current_screen):
    pygame.display.set_caption('Книга заклинаний')
    spells_book_generating = True
    current_screen = "magic_book"
    while spells_book_generating:
        screen.blit(pygame.image.load("nemeron_gates.jpg"), (-100, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spells_book_generating = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                activate_card_button_1.is_hovered = activate_card_button_1.position.collidepoint(pos)
                activate_card_button_2.is_hovered = activate_card_button_2.position.collidepoint(pos)
                activate_card_button_3.is_hovered = activate_card_button_3.position.collidepoint(pos)
                activate_card_button_4.is_hovered = activate_card_button_4.position.collidepoint(pos)
                activate_card_button_5.is_hovered = activate_card_button_5.position.collidepoint(pos)
                activate_card_button_6.is_hovered = activate_card_button_6.position.collidepoint(pos)
                activate_card_button_7.is_hovered = activate_card_button_7.position.collidepoint(pos)
                activate_card_button_8.is_hovered = activate_card_button_8.position.collidepoint(pos)
                activate_card_button_9.is_hovered = activate_card_button_9.position.collidepoint(pos)
                activate_card_button_10.is_hovered = activate_card_button_10.position.collidepoint(pos)
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "magic_book":
                    if activate_card_button_1.check_click(event.pos):
                        print("1")
                    if activate_card_button_2.check_click(event.pos):
                        print("2")
                    if activate_card_button_3.check_click(event.pos):
                        print("3")
                    if activate_card_button_4.check_click(event.pos):
                        print("4")
                    if activate_card_button_5.check_click(event.pos):
                        print("5")
                    if activate_card_button_6.check_click(event.pos):
                        print("6")
                    if activate_card_button_7.check_click(event.pos):
                        print("7")
                    if activate_card_button_8.check_click(event.pos):
                        print("8")
                    if activate_card_button_9.check_click(event.pos):
                        print("9")
                    if activate_card_button_10.check_click(event.pos):
                        print("10")
                    elif back_button2.check_click(event.pos):
                        current_screen = "training"

        if current_screen == "magic_book":
            activate_card_button_1.draw(screen)
            activate_card_button_2.draw(screen)
            activate_card_button_3.draw(screen)
            activate_card_button_4.draw(screen)
            activate_card_button_5.draw(screen)
            activate_card_button_6.draw(screen)
            activate_card_button_7.draw(screen)
            activate_card_button_8.draw(screen)
            activate_card_button_9.draw(screen)
            activate_card_button_10.draw(screen)
            back_button2.draw(screen)

        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen="training")
            break
        pygame.display.flip()

    #for i in cards_compilation:
    #    if i.active == 1:
def generate_exit(current_screen):
    screen.fill(BLACK)
    pygame.display.set_caption('Выход')
    screen.blit(background_image_to_name_input, (0, 0))
    running_exit = True
    while running_exit:
        screen.blit(background_image_to_name_input, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_exit = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_exit_button.is_hovered = back_exit_button.position.collidepoint(pos)
                real_exit_button.is_hovered = real_exit_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "exit":
                    if back_exit_button.check_click(event.pos):
                        current_screen = "menu"
                    elif real_exit_button.check_click(event.pos):
                        pygame.quit()
        if current_screen == "exit":
            pygame.display.set_caption('Подтверждение выхода')
            print_text("Вы уверены что хотите выйти из игры?", 300, 550, font_color=WHITE, size=50)
            back_exit_button.draw(screen)
            real_exit_button.draw(screen)
        elif current_screen == "menu":
            generate_menu(current_screen="menu")
        pygame.display.flip()

def generate_main(current_screen):
    screen.blit(background_image_to_start_screen, (0, 0))
    running_menu = True
    while running_menu:
        screen.blit(background_image_to_start_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                menu_button.is_hovered = menu_button.position.collidepoint(pos)
                start_button.is_hovered = start_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "main":
                    if start_button.check_click(event.pos):

                        pygame.display.set_caption('Об игре')
                        generate_about_game(current_screen="about_game")
                        #screen.blit(background_image_to_lor, (0, 0))
                    elif menu_button.check_click(event.pos):
                        generate_menu(current_screen = "menu")

        if current_screen == "main":
            start_button.draw(screen)
            menu_button.draw(screen)
        elif current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
        elif current_screen == "about_game":
            font = pygame.font.SysFont("Gabriola", 25)
            # '''
            text_introduction = ["Приветствую тебя, путник!",
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
                                 "",
                                 "Армии воинов, даже после своей смерти хранящих покой своих владык"]
            movement = 0
            for i in text_introduction:
                text_surf_1 = font.render(i, True, WHITE)
                screen.blit(text_surf_1, (25, 400 + movement))
                movement += 20
            # '''
            back_button2.draw(screen)
            next_button.draw(screen)
            '''
            text = "Введите имя вашего персонажа"
            font = pygame.font.SysFont(None, 50)
            text_surf_2 = font.render(text, True, WHITE)
            screen.blit(text_surf_2, (400, 600))
            '''
        pygame.display.flip()

def generate_about_game(current_screen):
    screen.blit(background_image_to_lor, (0, 0))
    running_about_game = True
    while running_about_game:
        screen.blit(background_image_to_lor, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_about_game = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
                next_button.is_hovered = next_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "about_game":
                    if back_button2.check_click(event.pos):
                        pygame.display.set_caption('Начальный экран')
                        generate_main(current_screen = "main")
                    elif next_button.check_click(event.pos):
                        pygame.display.set_caption('Обучение')
                        generate_training(current_screen = "training", player_position = player_position, last_player_position=last_player_position)
        if current_screen == "about_game":
            font = pygame.font.SysFont("Gabriola", 25)
            # '''
            text_introduction = ["Приветствую тебя, путник!",
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
                                 "",
                                 "Армии воинов, даже после своей смерти хранящих покой своих владык"]
            movement = 0
            for i in text_introduction:
                text_surf_1 = font.render(i, True, WHITE)
                screen.blit(text_surf_1, (25, 400 + movement))
                movement += 20
            # '''
            back_button2.draw(screen)
            next_button.draw(screen)
        if current_screen == "main":
            start_button.draw(screen)
            menu_button.draw(screen)
        elif current_screen == "training":
            generate_training(current_screen = "training", player_position = player_position, last_player_position=last_player_position)
        pygame.display.flip()

def generate_equipment(current_screen):
    pass

background_image_to_start_screen = pygame.image.load("ctulkhu.jpg")
background_image_to_name_input = pygame.image.load("nemeron_gates.jpg")
background_image_to_training_level_v1 = pygame.image.load("background_for_training_level_v2.jpg")
background_image_to_lor = pygame.image.load("page2.jpg")

#screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_map = pygame.Surface((SCREEN_WIDTH // MAP_SCALE, SCREEN_HEIGHT//MAP_SCALE))

pygame.display.set_caption('Начальный экран')

drawing = Drawing(screen, screen_map)
clock = pygame.time.Clock()

#players_nick = input("Введите имя вашего персонажа: ")
players_nick = "Ренион"

Player = Hero(  name           = players_nick,
                player_pos     = player_position,
                healthpoints   = 25,
                damage         = 5,
                armor          = 0,
                attack_range   = 1,
                movement_speed = 1,
                vision_distance= 3)

(current_map,
 current_player_map,
 current_player_vision_map,
 matrix_player_position_map,
 matrix_walls_map,
 matrix_player_vision_map)  =  training_level_layers_generate(map_width =  map_width, map_height = map_height, vis_distance = Player.vision_distance)

# Создаем отбражение здоровья
health_bar = StatusBar(20, 20, 50, 20, 0, 50, current_value=Player.healthpoints, text = "HP", color = RED)
# Создаем отбражение атаки
damage_bar = StatusBar(20, 40, 50, 20, 0, 30, current_value=Player.damage, text = "Attack", color = BLUE)
# Создаем отбражение дальности зрения
vision_distance_bar  = StatusBar(20, 60, 50, 20, 0, 10, current_value=Player.vision_distance, text="V_dist", color =GREEN )

all_cards = cards_initialization()
'''
for i in all_cards:
    i.print_card()
'''

generate_main(current_screen ="main")

generate_training(current_screen="training", player_position = player_position, last_player_position=last_player_position, matrix_walls_map=matrix_walls_map,matrix_player_vision_map = matrix_player_vision_map)

pygame.quit()