import operator
import json
import math
import numpy as np
import pygame
pygame.init()
# game settings

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_HALF_WIDTH = SCREEN_WIDTH // 2
SCREEN_HALF_HEIGHT = SCREEN_HEIGHT // 2

map_width = SCREEN_WIDTH // 25
map_height = SCREEN_HEIGHT // 25

# player settings
players_nick = "Ренион"

default_first_level_position = (17, 22)
last_player_position = (17, 22)

player_position = (17, 22)

player_speed = 5

player_angle = 0

FIELD_OF_VIEW = math.pi / 3

HALF_FIELD_OF_VIEW = FIELD_OF_VIEW / 2

NUM_RAYS_IN_FIELD_OF_VIEW = 120

DELTA_ANGLE = FIELD_OF_VIEW / NUM_RAYS_IN_FIELD_OF_VIEW

MAX_DEPTH = 200

FPS = 40
# map

TILE = SCREEN_HEIGHT // map_height
# TILE = 60

# mini map

MAP_SCALE = 5

MAP_TILE = TILE // MAP_SCALE

MAP_POSITION = (0, SCREEN_HEIGHT - SCREEN_HEIGHT // MAP_SCALE)

# ray_casting
SCALE = SCREEN_WIDTH // NUM_RAYS_IN_FIELD_OF_VIEW

# level settings
start_position_on_first_level = (14, 8)

# FPS settings
FPS_POSITION = (SCREEN_WIDTH - 65, 5)

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

screen_map = pygame.Surface(
    (SCREEN_WIDTH // MAP_SCALE,
     SCREEN_HEIGHT // MAP_SCALE))

pygame.display.set_caption('Начальный экран')

pygame.display.set_icon(pygame.image.load('pictures/icon.jpg'))

current_screen = "main"

#level layers
buffer_cur_NPC_pos_map = set()
buffer_matrix_NPC_pos_map = np.zeros((map_width, map_height))
buffer_set_NPC_coordinates=set()

# text
training_text_location_x = 640

training_text_location_y = 35

#break
break_1 =0
# colors

BLACK = (0, 0, 0)

DARKGRAY = (110, 110, 110)

WHITE = (255, 255, 255)

RED = (220, 0, 0)

ORANGE = (180, 140, 0)

YELLOW = (0, 120, 120)

GREEN = (0, 220, 0)

GREENS = (176, 212, 144)

DARK_GREEN = (54, 109, 9)

BLUE = (0, 0, 220)

PURPLE = (120, 0, 120)

DARK_PURPLE = (66, 25, 84)

DARK_BLUE = (34, 93, 92)

STATUS_BAR_TEXT_COLOR = (149, 204, 191)

BACKGROUND_STATUS_BAR_COLOR = (57, 98, 112)

STATUS_BAR_HP_BACKGROUND_COLOR = (87, 21, 39)

STATUS_BAR_DAMAGE_BACKGROUND_COLOR = (21, 72, 87)

STATUS_BAR_VISION_BACKGROUND_COLOR = (21, 87, 53)


# background images
background_image_to_magic_book = pygame.image.load("pictures/magic_book.jpg")
background_image_to_start_screen = pygame.image.load("pictures/main_page.jpeg")
background_image_to_pause = pygame.image.load("pictures/pause.jpg")
background_image_to_training_level = pygame.image.load(
    "pictures/training_level.jpg")
background_image_to_first_level = pygame.image.load("pictures/first_level.jpg")
background_image_to_about_game = pygame.image.load("pictures/about_game.jpg")
background_image_to_exit_game = pygame.image.load("pictures/exit_game.jpeg")
background_image_to_equipment = pygame.image.load("pictures/equipment.jpg")
background_image_to_quests = pygame.image.load("pictures/quests.jpg")
background_image_to_generate_end_of_game = pygame.image.load(
    "pictures/end_of_game.jpg")


def save_map_array_to_file(map_name, matrix_map, file):
    a = {}
    a.update({map_name: matrix_map})
    level_jsn = json.dumps(a)
    with open(file, 'w') as f:
        json.dump(level_jsn, f)


def load_map_array_from_file(map_name, file):
    f = open(file)
    buffer = json.load(f)
    map_dictionary = json.loads(buffer)
    matrix_map = map_dictionary[map_name]
    return (matrix_map)


def print_text(
    message,
    x,
    y,
    font_color,
    font_type=pygame.font.Font(
        'fonts/Mediteran.ttf',
        12),
        sc=pygame.display.set_mode(
            (SCREEN_WIDTH,
             SCREEN_HEIGHT),
        pygame.NOFRAME)):
    text_font_type = font_type
    text = text_font_type.render(message, True, font_color)
    sc.blit(text, (x, y))


def define_distance_between_2_positions(
        position_number_one,
        position_number_two):
    x1, y1 = position_number_one
    x2, y2 = position_number_two
    delta_x = math.fabs(x1 - x2)
    delta_y = math.fabs(y1 - y2)
    return (max(delta_x, delta_y))



class Magic_book:
    pass


class Cards:
    def __init__(self, card_name, discription, number, image, card_form):
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

    def __init__(
            self,
            name,
            healthpoints,
            damage,
            armor,
            attack_range,
            movement_speed,
            vision_distance,
            player_position):
        self.name = name
        self.x, self.y = player_position
        self.healthpoints = healthpoints
        self.damage = damage
        self.armor = armor
        self.attack_range = attack_range
        self.movement_speed = movement_speed
        self.vision_distance = vision_distance
        self.is_alive = True

    def movement(self, current_walls_map, current_decor_map, current_NPC_map):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # north
            if ((current_walls_map[self.x - 1][self.y] == 0 or current_walls_map[self.x - 1][self.y] == 9) and
                (current_NPC_map[self.x - 1][self.y] != 7 and current_decor_map[self.x - 1][self.y] != 4)):
                self.x += - self.movement_speed
                self.y += 0

        elif keys[pygame.K_s]:  # south
            if ((current_walls_map[self.x +1][self.y] == 0 or current_walls_map[self.x + 1][self.y] == 9) and
                (current_NPC_map[self.x +1][self.y] != 7 and current_decor_map[self.x +1][self.y] != 4)):
                self.x += self.movement_speed
                self.y += 0

        elif keys[pygame.K_a]:  # west
            if ((current_walls_map[self.x][self.y - 1] == 0 or current_walls_map[self.x][self.y -1] == 9) and
                    current_NPC_map[self.x][self.y - 1] != 7 and current_decor_map[self.x][self.y -1] != 4):
                self.x += 0
                self.y += -self.movement_speed

        elif keys[pygame.K_d]:  # east
            if ((current_walls_map[self.x][self.y + 1] == 0 or current_walls_map[self.x][self.y + 1] == 9) and
                    (current_NPC_map[self.x][self.y +1] != 7 and current_decor_map[self.x][self.y + 1] != 4)):
                self.x += 0
                self.y += self.movement_speed
        if current_walls_map[self.x][self.y] == 9:
            player_on_stages = True
        else:
            player_on_stages = False
        return (player_on_stages)
        # print(self.x, self.y)

    def take_damage (self, hit, matrix_NPC_position_map_in_take_damage = np.ones((map_height, map_width))):
        print("matrix_NPC_position_map_in_take_damage type = ", type(matrix_NPC_position_map_in_take_damage))
        print("matrix_NPC_position_map_in_take_damage size", len(matrix_NPC_position_map_in_take_damage))
        injury = hit
        #print("I am inside take damage function of Hero")
        if injury > 0:
            self.healthpoints -= injury
            if self.healthpoints <= 0:
                print("You died")
                pygame.quit()
                self.is_alive = False
                self.healthpoints = 0
        print('player_HP = ', self.healthpoints)

    def deal_damage(self,enemies, matrix_NPC_position_map_in_deal_damage = np.ones((map_height, map_width))):
        global break_1
        if (break_1 ==1):
            break_1=0
            return

        print("matrix_NPC_position_map_in_deal_damage type = ", type(matrix_NPC_position_map_in_deal_damage))
        print("matrix_NPC_position_map_in_deal_damage size", len(matrix_NPC_position_map_in_deal_damage))
        def attack(self, enemy, matrix_NPC_position_map_in_attack = matrix_NPC_position_map_in_deal_damage):
            print("matrix_NPC_position_map_in_attack type = ", type(matrix_NPC_position_map_in_attack))
            print("matrix_NPC_position_map_in_attack size", len(matrix_NPC_position_map_in_attack))
            hit = self.damage
            enemy.take_damage(hit, matrix_NPC_position_map_in_take_damage = matrix_NPC_position_map_in_attack)
            #global break_1
            if (break_1 == 1):
                return
        for i in range(len(enemies)-1):
            #print(len(enemies))
            distance_to_NPC = 1
            # distance_to_NPC = define_distance_between_2_positions(position_number_one= (self.x, self.y), position_number_two=(enemies[i].x, enemies[i].y))

            if distance_to_NPC <= 1.0:
                attack(self, enemy=enemies[i], matrix_NPC_position_map_in_attack= matrix_NPC_position_map_in_deal_damage)
            if (break_1 == 1):
                break
        if (break_1 == 1):
            return

    def take(self, matrix_decor_position_map = np.ones((map_height, map_width)) ):
        global break_1
        if (break_1 == 1):
            break_1 = 0
            return
        for i in range(len(matrix_decor_position_map)):
            for j in range(len(matrix_decor_position_map[i])):
                if (matrix_decor_position_map[i][j]!= 4):
                    #distance_to_decor = define_distance_between_2_positions((self.x, self.y), (i, j))
                    distance_to_decor = 1
                    #print("distance_to_decor = ", distance_to_decor)
                    if (distance_to_decor <= 1.0):
                        matrix_decor_position_map[i][j] = 0

        if (break_1 == 1):
            return(matrix_decor_position_map)


    def is_alive(self):
        return (self.is_alive)

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


class NPC:
    def __init__(
            self,
            name,
            healthpoints,
            damage,
            armor,
            attack_range,
            movement_speed,
            vision_distance,
            NPC_position):
        self.name = name
        self.x, self.y = NPC_position
        self.healthpoints = healthpoints
        self.damage = damage
        self.armor = armor
        self.attack_range = attack_range
        self.movement_speed = movement_speed
        self.vision_distance = vision_distance
        self.is_alive = True

    '''
    def movement(self, current_walls_map, current_decor_map, current_NPC_map):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # north
            if (current_walls_map[self.x - 1][self.y] == 0 or current_walls_map[self.x - 1][self.y] == 9) and \
                    current_NPC_map[self.x - 1][self.y] == 0 and current_decor_map[self.x - 1][self.y] == 0:
                self.x += -1
                self.y += 0


        elif keys[pygame.K_s]:  # south
            if (current_walls_map[self.x + 1][self.y] == 0 or current_walls_map[self.x + 1][self.y] == 9) and \
                    current_NPC_map[self.x + 1][self.y] == 0 and current_decor_map[self.x + 1][self.y] == 0:
                self.x += 1
                self.y += 0

        elif keys[pygame.K_a]:  # west
            if (current_walls_map[self.x][self.y - 1] == 0 or current_walls_map[self.x][self.y - 1] == 9) and \
                    current_NPC_map[self.x][self.y - 1] == 0 and current_decor_map[self.x][self.y - 1] == 0:
                self.x += 0
                self.y += -1

        elif keys[pygame.K_d]:  # east
            if (current_walls_map[self.x][self.y + 1] == 0 or current_walls_map[self.x][self.y + 1] == 9) and \
                    current_NPC_map[self.x][self.y + 1] == 0 and current_decor_map[self.x][self.y + 1] == 0:
                self.x += 0
                self.y += 1
        if current_walls_map[self.x][self.y] == 9:
            player_on_stages = True
        else:
            player_on_stages = False
        return (player_on_stages)
        '''
    # print(self.x, self.y)

    def take_damage(self, hit, matrix_NPC_position_map_in_take_damage = np.ones((map_height, map_width))):
        print("matrix_NPC_position_map_in_take_damage type = ", type(matrix_NPC_position_map_in_take_damage))
        print("matrix_NPC_position_map_in_take_damage size", len(matrix_NPC_position_map_in_take_damage))
        injury = hit
        #print("I am inside take damage function of NPC")
        if injury > 0:
            self.healthpoints -= injury
            if self.healthpoints <= 0:
                print("You kill the enemy")
                print("matrix_NPC_position_map_in_take_damage type", type(matrix_NPC_position_map_in_take_damage))
                print("matrix_NPC_position_map_in_take_damage size ", len(matrix_NPC_position_map_in_take_damage))
                update_NPC_level_layer(matrix_NPC_position_map_in_update_NPC_level_layers = matrix_NPC_position_map_in_take_damage)

                self.is_alive = False
                self.healthpoints = 0
        print('NPC_HP = ', self.healthpoints)
        global break_1
        break_1 = 1
        return

    def deal_damage(self, enemies, matrix_NPC_position_map_in_deal_damage =np.ones((map_height, map_width))):
        #print(*matrix_NPC_position_map_in_deal_damage)
        #print(type(matrix_NPC_position_map_in_deal_damage))
        def attack(self, enemy,matrix_NPC_position_map_in_attack= matrix_NPC_position_map_in_deal_damage):
            hit = self.damage
            enemy.take_damage(hit, matrix_NPC_position_map_in_take_damage = matrix_NPC_position_map_in_attack)

        for i in range(len(enemies)-1):

            #print(len(enemies))
            distance_to_NPC = 1
            # distance_to_NPC = define_distance_between_2_positions(position_number_one= (self.x, self.y), position_number_two=(enemies[i].x, enemies[i].y))

            if distance_to_NPC <= 1.0:
                attack(self, enemy=enemies[i], matrix_NPC_position_map_in_attack=[])

    def take(self, any_gold_position):
        # if (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]) or (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]):
        # all gold and medallions that are in surrounding square puts into
        # backpack
        pass

    def is_alive(self):
        return (self.is_alive)

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
        self.font = pygame.font.Font('fonts/Mediteran.ttf', 26)
        self.width, self.height = 200, 60
        self.position = pygame.Rect(position, (self.width, self.height))
        self.is_hovered = False

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            GREENS if self.is_hovered else DARK_BLUE,
            self.position)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.position.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, pos):
        if self.position.collidepoint(pos):
            return True
        return False


class StatusBar:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        min_value,
        max_value,
        current_value,
        text,
        color=(
            200,
            200,
            200)):
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
        pygame.draw.rect(
            screen,
            color=(BACKGROUND_STATUS_BAR_COLOR),
            rect=(
                self.x,
                self.y,
                self.width,
                self.height))

        # Рассчитываем ширину ползунка в зависимости от значений
        range = self.max_value - self.min_value
        value_offset = self.current_value - self.min_value
        slider_width = int((value_offset / range) * self.width)

        # Отрисовываем ползунок статус бара
        pygame.draw.rect(
            screen,
            color=self.color,
            rect=(
                self.x,
                self.y,
                slider_width,
                self.height))

        # Отрисовка текста
        print_text(
            message=self.text,
            x=self.x,
            y=self.y,
            font_color=STATUS_BAR_TEXT_COLOR,
            font_type=pygame.font.Font(
                'fonts/RAINFALL Black.otf',
                12))

    def update_value(self, new_value):
        # Обновляем текущее значение статус бара
        self.current_value = new_value


# создание кнопок
# начальный экран
start_button = Button("Начать игру", (260, 260))
start_button.width, start_button.height = 400, 100
start_button.position = pygame.Rect(
    (80, 140), (start_button.width, start_button.height))
menu_button = Button("Меню", (80, 220))
menu_button.width, menu_button.height = 200, 80
menu_button.position = pygame.Rect(
    (180, 260), (menu_button.width, menu_button.height))

# об игре
back_button2 = Button("Назад", (50, 700))
next_button = Button("Далее", (950, 700))

# меню
back_button = Button("На начальный экран", (40, 700))
back_button.font = pygame.font.Font('fonts/Mediteran.ttf', 12)
about_button = Button("Об авторах", (260, 700))
back_button3 = Button("К игре", (500, 700))
settings_button = Button("Настройки", (720, 700))
exit_button = Button("Выйти", (940, 700))

# выход
back_exit_button = Button("Остаться", (60, 350))
back_exit_button.font = pygame.font.Font(
    'fonts/AlgerianBasD [Rus by me] Regular.otf', 26)
real_exit_button = Button("Выйти", (560, 350))
real_exit_button.font = pygame.font.Font(
    'fonts/AlgerianBasD [Rus by me] Regular.otf', 26)

# пауза
magic_book_button = Button("Книга заклинаний", (500, 200))
magic_book_button.font = pygame.font.Font('fonts/Mediteran.ttf', 16)
quests_button = Button("Квесты", (500, 300))
equipment_button = Button("Инвентарь", (500, 400))
exit_button_2 = Button("Выйти в главное меню", (500, 700))
exit_button_2.font = pygame.font.Font('fonts/Mediteran.ttf', 12)
back_to_level_button = Button("Продолжить игру", (500, 500))
back_to_level_button.font = pygame.font.Font('fonts/Mediteran.ttf', 16)

# книга заклинаний
activate_card_button_1 = Button("Активировать", (40, 240))
activate_card_button_1.width, activate_card_button_1.height = 200, 40
activate_card_button_2 = Button("Активировать", (270, 240))
activate_card_button_2.width, activate_card_button_2.height = 200, 40
activate_card_button_3 = Button("Активировать", (500, 240))
activate_card_button_3.width, activate_card_button_3.height = 200, 40
activate_card_button_4 = Button("Активировать", (730, 240))
activate_card_button_4.width, activate_card_button_4.height = 200, 40
activate_card_button_5 = Button("Активировать", (960, 240))
activate_card_button_5.width, activate_card_button_5.height = 200, 40
activate_card_button_6 = Button("Активировать", (40, 620))
activate_card_button_6.width, activate_card_button_6.height = 200, 40
activate_card_button_7 = Button("Активировать", (270, 620))
activate_card_button_7.width, activate_card_button_7.height = 200, 40
activate_card_button_8 = Button("Активировать", (500, 620))
activate_card_button_8.width, activate_card_button_8.height = 200, 40
activate_card_button_9 = Button("Активировать", (730, 620))
activate_card_button_9.width, activate_card_button_9.height = 200, 40
activate_card_button_10 = Button("Активировать", (960, 620))
activate_card_button_10.width, activate_card_button_10.height = 200, 40


class Drawing:
    def __init__(self, sc, sc_map):

        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.Font('fonts/Mediteran.ttf', 36)

    def fps_drawing(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, YELLOW)
        self.sc.blit(render, FPS_POSITION)

    def draw_walls(self, sc, cur_map):
        for x, y in cur_map:
            pygame.draw.rect(sc, RED, (x, y, TILE, TILE), TILE)

    def draw_player(self, sc, player_pos, cur_player_pos):
        player_avatar_image = pygame.image.load('elf sprites/tile020.png')
        #x, y = player_pos
        for x, y in cur_player_pos:
            sc.blit(player_avatar_image, (x - 2, y - 6))
            # pygame.draw.circle(sc, GREEN, (x+TILE//2, y+TILE//2), TILE//2)
            # pygame.draw.circle(sc, BLACK, (x+TILE//2, y+TILE//2), TILE//2, 2)

    def draw_player_vision(self, sc, cur_player_vis_map):
        for x, y in cur_player_vis_map:
            pygame.draw.rect(sc, (BLACK), (x, y, TILE, TILE), TILE)

    def draw_NPC(self, sc, cur_NPC_pos_map):

        enemy_avatar_image = pygame.image.load('enemy sprites/enemy_from_training_level.png')
        for x, y in cur_NPC_pos_map:
            #pygame.draw.circle(sc, RED, (x + TILE // 2, y + TILE // 2), TILE // 2)
            #pygame.draw.circle(sc, BLACK, (x + TILE // 2, y + TILE // 2), TILE // 2, 2)
            sc.blit(enemy_avatar_image, (x - 2, y - 6))
    def draw_NPC_based_on_matrix(self, sc, matrix_NPC_pos_map):
        enemy_avatar_image = pygame.image.load('enemy sprites/enemy_from_training_level.png')
        for y in range (1,len(matrix_NPC_pos_map)+1):
            for x in range (1, len(matrix_NPC_pos_map[0])+1):
                if (matrix_NPC_pos_map[y-1][x-1]==7):
                    sc.blit(enemy_avatar_image, (x*25 - 28, y*25 - 32))
                    #pygame.draw.circle(sc, RED, (x*25 -( TILE // 2), y*25 - (TILE // 2)), TILE // 2)
                    #pygame.draw.circle(sc, BLACK, (x *25- (TILE // 2), y*25 - (TILE // 2)), TILE // 2, 2)

    def draw_decor(self, sc, cur_dec_pos_map):
        for x, y in cur_dec_pos_map:
            pygame.draw.circle(sc, BLUE, (x + TILE // 2, y + TILE // 2), TILE // 2)
            pygame.draw.circle(sc, BLACK, (x + TILE // 2, y + TILE // 2), TILE // 2, 2)
            pass

    def draw_rect(self, screen):
        # Отрисовка фона статус бара
        pygame.draw.rect(screen, color=(220, 220, 220), rect=(0, 0, 1200, 800))


'''import_data_from_files'''
matrix_walls_position_map_training_level = load_map_array_from_file(
    map_name='matrix_walls_map_training_level',
    file='matrix_walls_map_training_level.json')
matrix_walls_position_map_first_level = load_map_array_from_file(
    map_name='matrix_walls_map_first_level',
    file='matrix_walls_map_first_level.json')

# Функции инициализации


def level_layers_initialization(
        map_width,
        map_height,
        vis_distance,
        map_name,
        file,
        player_position=player_position):

    # player_pos
    # слой с отображением позиции игрока
    matrix_player_pos_map = np.zeros((map_height, map_width))
    matrix_player_pos_map[player_position] = 1
    last_player_position = player_position
    # print(matrix_player_pos_map, '\n')
    ''''''
    # создаём стек используемых для прорисовки позиции игрока точек
    cur_player_pos_on_map = matrix_player_pos_map
    cur_player_pos_map = set()
    for j, row in enumerate(cur_player_pos_on_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_pos_map.add((i * TILE, j * TILE))

    # wal
    # слой с изображением стен
    # matrix_wal_map = (np.ones((map_height, map_width)))
    # внешняяя стена вокруг
    # matrix_wal_map[1:-1,1:-1:] = 0
    # внутренние стены
    # matrix_wal_map[5:-5,5:-5:] = 1
    matrix_wal_map = load_map_array_from_file(map_name, file)
    # print(matrix_wal_map, '\n')
    ''''''
    # создаём стек используемых для прорисовки квадратиков стен точек
    cur_matrix_wal_map = matrix_wal_map
    cur_wal_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_wal_map.add((i * TILE, j * TILE))

    # vis
    # создаём слой видимости игроком
    # слой с отображением позиции игрока
    matrix_player_vis_map = (np.ones((map_height, map_width)))
    matrix_player_vis_map[last_player_position] = 1
    last_player_position = player_position
    matrix_player_vis_map[(player_position[0] -
                           vis_distance):(player_position[0] +
                                          vis_distance +
                                          1), (player_position[1] -
                                               vis_distance): (player_position[1] +
                                                               vis_distance +
                                                               1):] = 0
    matrix_player_vis_map[(player_position[0] -
                           1):(player_position[0] +
                               1 +
                               1), (player_position[1] -
                                    1): (player_position[1] +
                                         1 +
                                         1):] = 0
    matrix_player_vis_map[(player_position[0] -
                           2):(player_position[0] +
                               2 +
                               1), (player_position[1] -
                                    2): (player_position[1] +
                                         2 +
                                         1):] = 0
    # print(*matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки зрения игрока точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))

    # dec
    # создаём наполнение/декор
    matrix_dec_pos_map = np.zeros((map_height, map_width))
    matrix_dec_pos_map[16, 17] = 4
    matrix_dec_pos_map[10, 23] = 4
    ''''''
    # создаём стек используемых для прорисовки позиции декора точек
    cur_dec_pos_on_map = matrix_dec_pos_map
    cur_dec_pos_map = set()
    for j, row in enumerate(cur_dec_pos_on_map):
        for i, number in enumerate(row):
            if number == 4:
                cur_dec_pos_map.add((i * TILE, j * TILE))

    # NPC
    # создаём слой расположения всех NPC уровня и экземпляр класса NPC на
    # каждую точку создаём NPC
    matrix_NPC_pos_map = np.zeros((map_height, map_width))
    test_NPC_position =(17, 3)
    test_NPC_position_2 = (15, 29)
    matrix_NPC_pos_map[test_NPC_position] = 7
    matrix_NPC_pos_map[test_NPC_position_2] = 7
    #print(*matrix_NPC_pos_map)
    global buffer_matrix_NPC_pos_map
    buffer_matrix_NPC_pos_map = matrix_NPC_pos_map

    # load_from_file_NPC_map
    enemy_1 = NPC_initialization(NPC_position=(test_NPC_position), NPC_type=matrix_NPC_pos_map[test_NPC_position])
    enemies_of_level = [enemy_1]  # Список экземпляров класса
    #for i in enemies_of_level:
    #    print(i)
    enemies_of_level.sort(key=lambda enemies_of_level: enemies_of_level.x) # Сортировка по атрибуту name
    for enemy in enemies_of_level:
        print("enemy.healthpoints = ", enemy.healthpoints)
        pass

    for i in range(len(matrix_NPC_pos_map)):
        for j in range(len(matrix_NPC_pos_map[i])):
            if matrix_NPC_pos_map[i][j] != 0:
                enemies_of_level.append(
                    NPC_initialization(
                        NPC_position=(
                            i, j), NPC_type=matrix_NPC_pos_map[i][j]))
                #print("enemy_of_level",NPC_initialization(NPC_position=(i,j),NPC_type=matrix_NPC_pos_map[i][j]))

    # создаём стек используемых для прорисовки позиции NPC точек

    cur_NPC_pos_on_map = matrix_NPC_pos_map
    cur_NPC_pos_map = set()
    set_NPC_coordinates = set()
    for j, row in enumerate(cur_NPC_pos_on_map):
        for i, number in enumerate(row):
            if number == 8:
                cur_NPC_pos_map.add((i * TILE, j * TILE))
                set_NPC_coordinates.add((i, j))

    return (cur_player_pos_map,
            cur_wal_map,
            cur_player_vis_map,
            cur_dec_pos_map,
            cur_NPC_pos_map,

            matrix_player_pos_map,
            matrix_wal_map,
            matrix_player_vis_map,
            matrix_dec_pos_map,
            matrix_NPC_pos_map,

            set_NPC_coordinates,
            enemies_of_level)


def enemy_initialization(
        name,
        healthpoints,
        damage,
        armor,
        attack_range,
        movement_speed,
        vision_distance,
        enemy_position):
    enemy = NPC(name=players_nick,
                healthpoints=25,
                damage=10,
                armor=0,
                attack_range=1,
                movement_speed=1,
                vision_distance=3,
                NPC_position=enemy_position)


def cards_initialization():
    mythryl_sword = Cards(
        card_name='Мифриловый меч',
        discription="",
        number=1,
        image="",
        card_form="")
    fog_lion = Cards(
        card_name="Туманный лев",
        discription="",
        number=2,
        image="",
        card_form="")
    grakula = Cards(
        card_name="Гракула",
        discription="",
        number=3,
        image="",
        card_form="")
    sprigan = Cards(
        card_name="Сприган. мастер ловушек",
        discription="",
        number=4,
        image="",
        card_form="")
    crystal_mole = Cards(
        card_name="Кристаллический крот",
        discription="",
        number=5,
        image="",
        card_form="")
    kayrun_hammer = Cards(
        card_name="Молот Кайруна",
        discription="",
        number=6,
        image="",
        card_form="")
    wind_of_ice_debris = Cards(
        card_name="Ветер ледяных осколков",
        discription="",
        number=7,
        image="",
        card_form="")
    breath_of_dragons_ancestors = Cards(
        card_name="Дыхание прародителей драконов",
        discription="",
        number=8,
        image="",
        card_form="")
    giant_eye = Cards(
        card_name="Глаз исполина",
        discription="",
        number=9,
        image="",
        card_form="")
    armor_of_rapid_strikes = Cards(
        card_name="Доспех стремительных ударов",
        discription="",
        number=10,
        image="",
        card_form="")
    '''
    =Cards(card_name="", discription="")
    '''
    all_cards = [mythryl_sword,
                 fog_lion,
                 grakula,
                 sprigan,
                 crystal_mole,
                 kayrun_hammer,
                 wind_of_ice_debris,
                 breath_of_dragons_ancestors,
                 giant_eye,
                 armor_of_rapid_strikes]
    '''
    for i in all_cards:
        i.print_card()
    '''
    return (all_cards)


def status_bar_initialization():
    # Создаем отбражение здоровья
    health_bar = StatusBar(
        20,
        20,
        50,
        20,
        0,
        50,
        current_value=Player.healthpoints,
        text="HP",
        color=STATUS_BAR_HP_BACKGROUND_COLOR)
    # Создаем отбражение атаки
    damage_bar = StatusBar(
        20,
        40,
        50,
        20,
        0,
        30,
        current_value=Player.damage,
        text="Attack",
        color=STATUS_BAR_DAMAGE_BACKGROUND_COLOR)
    # Создаем отбражение дальности зрения
    vision_distance_bar = StatusBar(
        20,
        60,
        50,
        20,
        0,
        10,
        current_value=Player.vision_distance,
        text="vision",
        color=STATUS_BAR_VISION_BACKGROUND_COLOR)
    return (health_bar, damage_bar, vision_distance_bar)


def hero_initialization():
    Player = Hero(name=players_nick,
                  player_position=player_position,
                  healthpoints=25,
                  damage=5,
                  armor=0,
                  attack_range=1,
                  movement_speed=1,
                  vision_distance=3)
    return (Player)


def NPC_initialization(NPC_position=(17, 17), NPC_type=7):
    if NPC_type == 7:
        NPC_of_level = NPC(name="Пепельник",
                           NPC_position=NPC_position,
                           healthpoints=30,
                           damage=4,
                           armor=2,
                           attack_range=3,
                           movement_speed=1,
                           vision_distance=3)
        return (NPC_of_level)


def decor_initialization():
    pass


# Функции окон первого уровня
def choose_window_generation(current_screen):
    match current_screen:
        case "main":
            print('generate_main(current_screen = "main")')
            current_screen_inside_choose_window_generation = generate_main(
                current_screen="main")
            return (current_screen_inside_choose_window_generation)
        case "menu":
            print('generate_menu(current_screen = "menu")')
            current_screen_inside_choose_window_generation = generate_menu(
                current_screen="menu")
            return (current_screen_inside_choose_window_generation)
        case "about_game":
            print('generate_about_game(current_screen = "about_game")')
            current_screen_inside_choose_window_generation = generate_about_game(
                current_screen="about_game")
            return (current_screen_inside_choose_window_generation)
        case "training":
            print('generate_training(current_screen = "training", player_position = player_position, last_player_position=last_player_position')
            current_screen_inside_choose_window_generation = generate_training(
                current_screen="training",
                player_position=player_position,
                last_player_position=last_player_position)
            return (current_screen_inside_choose_window_generation)
        case "first_level":
            print('generate_first_level(current_screen="first_level", player_position = player_position, last_player_position=last_player_position, matrix_walls_map=matrix_walls_position_map_first_level, matrix_player_vision_map=np.ones(map_height, map_width))')
            current_screen_inside_choose_window_generation = generate_first_level(
                current_screen="first_level",
                player_position=player_position,
                last_player_position=last_player_position)
            return (current_screen_inside_choose_window_generation)
        case"exit":
            print('generate_exit(current_screen = "exit")')
            current_screen_inside_choose_window_generation = generate_exit(
                current_screen="exit")
            return (current_screen_inside_choose_window_generation)
        case "end_of_game":
            print('generate_end_of_game(current_screen = "end_of_game")')
            current_screen_inside_choose_window_generation = generate_end_of_game(
                current_screen="end_of_game")
            return (current_screen_inside_choose_window_generation)


def generate_main(current_screen):
    screen.blit(background_image_to_start_screen, (0, 0))
    running_main_page = True
    while running_main_page:
        screen.blit(background_image_to_start_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_main_page = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                menu_button.is_hovered = menu_button.position.collidepoint(pos)
                start_button.is_hovered = start_button.position.collidepoint(
                    pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "main":
                    if start_button.check_click(event.pos):
                        pygame.display.set_caption('Об игре')
                        current_screen = "about_game"
                        running_main_page = False
                        return (current_screen)
                        # screen.blit(background_image_to_lor, (0, 0))
                    elif menu_button.check_click(event.pos):
                        current_screen = "menu"
                        running_main_page = False
                        return (current_screen)

        if current_screen == "main":
            start_button.draw(screen)
            menu_button.draw(screen)

        elif current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
        elif current_screen == "about_game":
            font = pygame.font.Font('fonts/Mediteran.ttf', 25)

            text_introduction = [
                "Приветствую тебя, путник!",
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

            back_button2.draw(screen)
            next_button.draw(screen)

        pygame.display.flip()


def generate_menu(current_screen):
    pygame.display.set_caption('Меню')
    screen.blit(background_image_to_about_game, (0, 0))
    running_menu = True
    while running_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                settings_button.is_hovered = settings_button.position.collidepoint(
                    pos)
                exit_button.is_hovered = exit_button.position.collidepoint(pos)
                back_button.is_hovered = back_button.position.collidepoint(pos)
                back_button3.is_hovered = back_button3.position.collidepoint(
                    pos)
                about_button.is_hovered = about_button.position.collidepoint(
                    pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "menu":

                    if back_button.check_click(event.pos):
                        current_screen = "main"
                        return (current_screen)
                    elif exit_button.check_click(event.pos):
                        current_screen = "exit"
                        return (current_screen)
                    elif back_button3.check_click(event.pos):
                        current_screen = "training"
                        return (current_screen)
                    elif settings_button.check_click(event.pos):
                        print("Открыть окно настроек")
                    elif about_button.check_click(event.pos):
                        print("Студенты группы ББСО-01-22")
                        print("Дубинин И. П.")
                        print("Концов С. А.")
            if (running_menu== True):
                print_text(
                    message="Меню",
                    x=training_text_location_x - 60,
                    y=training_text_location_y - 25,
                    font_color=WHITE)


        if current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
            back_button3.draw(screen)

        elif current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            generate_main(current_screen="main")
        elif current_screen == "exit":
            pygame.display.set_caption('Выход')
            generate_exit(current_screen="exit")
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen="training")

        pygame.display.flip()


def generate_about_game(current_screen):
    screen.blit(background_image_to_about_game, (0, 0))
    running_about_game = True
    while running_about_game:
        screen.blit(background_image_to_about_game, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_about_game = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(
                    pos)
                next_button.is_hovered = next_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "about_game":
                    if back_button2.check_click(event.pos):
                        pygame.display.set_caption('Начальный экран')
                        current_screen = "main"
                        running_about_game = False
                        return (current_screen)
                    elif next_button.check_click(event.pos):
                        pygame.display.set_caption('Обучение')
                        current_screen = "training"
                        running_about_game = False
                        return (current_screen)
        if current_screen == "about_game":
            background_field = pygame.Surface(
                (1200, 300))  # the size of your rect
            background_field.set_alpha(128)  # alpha level
            screen.blit(background_field, (0, 380))
            font = pygame.font.Font('fonts/Mediteran.ttf', 12)
            # '''
            text_introduction = [
                "Приветствую тебя, путник!",
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
                "Армии воинов, даже после своей смерти хранят покой своих Владык"]
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
            generate_training(
                current_screen="training",
                player_position=player_position,
                last_player_position=last_player_position)
        pygame.display.flip()


def generate_training(
        current_screen="training",
        player_position=player_position,
        last_player_position=last_player_position,
        matrix_walls_map=matrix_walls_position_map_training_level):
    pygame.display.set_caption('Тренировка')
    screen.blit(background_image_to_training_level, (0, 0))

    (current_player_position_map,
     current_walls_position_map,
     current_player_vision_map,
     current_decor_position_map,
     current_NPC_position_map,
     matrix_player_position_map,
     matrix_walls_position_map_training_level,
     matrix_player_vision_map,
     matrix_decor_position_map,
     matrix_NPC_position_map,
     any_NPC_position,
     enemies_of_level) = level_layers_initialization(map_width=map_width,
                                                     map_height=map_height,
                                                     vis_distance=Player.vision_distance,
                                                     map_name='matrix_walls_map_training_level',
                                                     file='matrix_walls_map_training_level.json')

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
    running_I_training = False
    running_Q_training = False

    stop_training = False
    current_screen = "training"
    while running_training:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running_training = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                current_screen = generate_quests("quests")
            if keys[pygame.K_m]:
                pygame.display.set_caption('Меню')
                current_screen = generate_menu(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                current_screen = generate_magic_book(
                    cards_compilation=all_cards, current_screen="magic_book")

            if keys[pygame.K_p]:
                pygame.display.set_caption('Пауза')
                current_screen = generate_pause(current_screen="pause")
            if keys[pygame.K_i]:
                pygame.display.set_caption('Снаряжение')
                current_screen = generate_equipment(current_screen="equipment")
            if keys[pygame.K_f]:
                matrix_NPC_position_map= list(matrix_NPC_position_map)
                Player.deal_damage(enemies = enemies_of_level, matrix_NPC_position_map_in_deal_damage = matrix_NPC_position_map)
                global buffer_cur_NPC_pos_map
                #print("buffer_cur_NPC_pos_map ", buffer_cur_NPC_pos_map)
                #print("buffer_cur_NPC_pos_map type", type(buffer_cur_NPC_pos_map))
                current_NPC_position_map = buffer_cur_NPC_pos_map
                #buffer_cur_NPC_pos_map = []
                global buffer_matrix_NPC_pos_map
                #print("matrix_NPC_position_map", *matrix_NPC_position_map)
                matrix_NPC_position_map = buffer_matrix_NPC_pos_map
                #buffer_matrix_NPC_pos_map = []

            '''
            if keys[pygame.K_t]:
                print(*matrix_decor_position_map)
                matrix_decor_position_map = Player.take(matrix_decor_position_map= matrix_decor_position_map)
                print(matrix_decor_position_map)
            '''
            (
                current_walls_position_map,
                current_player_map,
                current_player_vision_map,
                matrix_player_position_map,
                matrix_walls_map,
                matrix_player_vision_map) = update_major_level_layers(
                last_player_pos=last_player_position,
                player_position=player_position,
                matrix_walls_map=matrix_walls_map,
                matrix_player_vision_map=matrix_player_vision_map,
                vis_distance=Player.vision_distance)


            current_NPC_position_map = buffer_cur_NPC_pos_map
            #print("current_NPC_position_map_after_major_layers_update ", current_NPC_position_map)
            matrix_NPC_position_map = buffer_matrix_NPC_pos_map
            #print("matrix_NPC_position_map_after_major_layers_update ", matrix_NPC_position_map)
            '''Отрисовка'''
            # clock.tick(60)
            screen.fill(BLACK)
            screen.blit(background_image_to_training_level, (0, 0))
            #drawing.draw_walls(sc= screen, cur_map = current_walls_position_map)
            drawing.draw_player(sc=screen,
                                player_pos=player_position,
                                cur_player_pos=current_player_map)
            #print(*matrix_decor_position_map)
            drawing.draw_decor(
                sc=screen, cur_dec_pos_map=current_decor_position_map)
            #print(*matrix_NPC_position_map)
            drawing.draw_NPC(
                sc=screen, cur_NPC_pos_map=current_NPC_position_map)
            drawing.draw_NPC_based_on_matrix(sc=screen, matrix_NPC_pos_map = matrix_NPC_position_map)
            drawing.draw_player_vision(
                sc=screen, cur_player_vis_map=current_player_vision_map)
            drawing.fps_drawing(clock)

            player_on_stages = Player.movement(
                matrix_walls_map,
                matrix_decor_position_map,
                matrix_NPC_position_map)
            if player_on_stages:
                Player.x, Player.y = start_position_on_first_level
                player_position = start_position_on_first_level
                drawing.draw_player_vision(
                    sc=screen, cur_player_vis_map=current_player_vision_map)
                current_screen = "first_level"
                return (current_screen)
            player_position = (Player.x, Player.y)

            background_field = pygame.Surface(
                (400, 90))  # the size of your rect
            background_field.set_alpha(234)  # alpha level
            screen.blit(
                background_field,
                (training_text_location_x - 64,
                 training_text_location_y - 35))

            '''обучение перемещению'''

            if (running_W_training == 1):
                print_text(
                    message="Чтобы двинуться вперёд, нажмите W",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_w]:
                    running_W_training = False
                    running_S_training = True
                    pass
            if (running_S_training == 1):
                print_text(
                    message="Чтобы двинуться назад, нажмите S",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_s]:
                    running_S_training = False
                    running_A_training = True
                    pass
            if (running_A_training == 1):
                print_text(
                    message="Чтобы двинуться влево, нажмите A",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_a]:
                    running_A_training = False
                    running_D_training = True
                    pass
            if (running_D_training == 1):
                print_text(
                    message="Чтобы двинуться вправо, нажмите D",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_d]:
                    running_D_training = False
                    # running_F_training = True #comment after pause editing
                    running_P_training = True
                    pass

            # обучение вариантам взаимодействия с окружением
            if (running_F_training == 1):
                print_text(
                    message="F позволит нанести удар",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_f]:
                    running_F_training = False
                    running_T_training = True
                    pass
            if (running_T_training == 1):
                print_text(
                    message="Чтобы взять предмет, нажмите  T",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_t]:
                    running_T_training = False
                    running_M_training = True
                    pass

            # обучение открытию окон
            if (running_P_training == 1):
                print_text(
                    message="Чтобы остановить игру, нажмите P",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_p]:
                    running_P_training = False
                    running_F_training = True
            if (running_M_training == 1):
                print_text(
                    message="Чтобы открыть меню, нажмите  M",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_m]:
                    running_M_training = False
                    running_B_training = True
                    pygame.display.set_caption('Меню')
                    current_screen = "menu"
                    pass
            if (running_B_training == 1):
                print_text(
                    message="Чтобы открыть книгу заклинаний, нажмите  B",
                    x=training_text_location_x - 40,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_b]:
                    running_B_training = False
                    running_I_training = True
                    pygame.display.set_caption('Книга заклинаний')
                    current_screen = "magic_book"
                    pass
            if (running_I_training == 1):
                print_text(
                    message="Чтобы открыть инвентарь, нажмите  I",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_i]:
                    running_I_training = False
                    running_Q_training = True
                    pygame.display.set_caption('Инвентарь')
                    current_screen = "equipment"
                    pass
            if (running_Q_training == 1):
                print_text(
                    message="Чтобы открыть квесты, нажмите  Q",
                    x=training_text_location_x,
                    y=training_text_location_y,
                    font_color=WHITE)
                if keys[pygame.K_q]:
                    running_Q_training = False
                    running_training = True
                    pygame.display.set_caption('Инвентарь')
                    current_screen = "equipment"
                    pass

            if (stop_training == False):
                print_text(
                    message="Чтобы пропустить обучение, нажмите Backspace",
                    x=training_text_location_x - 60,
                    y=training_text_location_y - 25,
                    font_color=WHITE)
                if keys[pygame.K_BACKSPACE]:
                    current_screen = "first_level"
                    Player.x, Player.y = start_position_on_first_level
                    player_position = start_position_on_first_level
                    # print(matrix_player_vision_map)
                    return (current_screen)
        if current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            return (current_screen)
        if (Player.x > 5 or Player.y > 5):
            health_bar.draw(screen)
            damage_bar.draw(screen)
            vision_distance_bar.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def generate_first_level(
        current_screen="first_level",
        player_position=player_position,
        last_player_position=last_player_position,
        matrix_walls_map=matrix_walls_position_map_first_level):
    pygame.display.set_caption('1 уровень')
    player_position = start_position_on_first_level
    screen.blit(background_image_to_first_level, (0, 0))
    (current_player_position_map,
     current_walls_position_map,
     current_player_vision_map,
     current_decor_position_map,
     current_NPC_position_map,
     matrix_player_position_map,
     matrix_walls_position_map_first_level,
     matrix_player_vision_map,
     matrix_decor_position_map,
     matrix_NPC_position_map,
     any_NPC_position,
     enemies_of_level) = level_layers_initialization(map_width=map_width,
                                                     map_height=map_height,
                                                     vis_distance=Player.vision_distance,
                                                     map_name='matrix_walls_map_training_level',
                                                     file='matrix_walls_map_training_level.json',
                                                     player_position=player_position)

    running_first_level = True
    while running_first_level:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running_first_level = False
                current_screen = "main"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                current_screen = generate_quests("quests")
            if keys[pygame.K_m]:
                pygame.display.set_caption('Меню')
                current_screen = generate_menu(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                current_screen = generate_magic_book(
                    cards_compilation=all_cards, current_screen="magic_book")

            if keys[pygame.K_p]:
                pygame.display.set_caption('Пауза')
                current_screen = generate_pause(current_screen="pause")
            if keys[pygame.K_i]:
                pygame.display.set_caption('Снаряжение')
                current_screen = generate_equipment(current_screen="equipment")
            # print(*matrix_player_vision_map)

            (
                current_walls_position_map,
                current_player_map,
                current_player_vision_map,
                matrix_player_position_map,
                matrix_walls_map,
                matrix_player_vision_map) = update_major_level_layers(
                last_player_pos=last_player_position,
                player_position=player_position,
                matrix_walls_map=matrix_walls_map,
                matrix_player_vision_map=matrix_player_vision_map,
                vis_distance=Player.vision_distance)
            if keys[pygame.K_f]:
                Player.deal_damage(self, enemies = enemies_of_level, matrix_NPC_position_map = matrix_NPC_position_map)
                current_NPC_position_map = buffer_cur_NPC_pos_map
                #buffer_cur_NPC_pos_map = []
                matrix_NPC_position_map = buffer_matrix_NPC_pos_map
                #buffer_matrix_NPC_pos_map = []

            if keys[pygame.K_BACKSPACE]:
                current_screen = "end_of_game"
                Player.x, Player.y = start_position_on_first_level
                player_position = start_position_on_first_level
                # print(matrix_player_vision_map)
                return (current_screen)
            '''Отрисовка'''
            screen.fill(BLACK)
            screen.blit(background_image_to_first_level, (0, 0))
            # drawing.draw_walls(sc= screen, cur_map = current_walls_position_map)
            # clock.tick(60)

            drawing.draw_player(sc=screen,
                                player_pos=player_position,
                                cur_player_pos=current_player_map)
            drawing.draw_decor(
                sc=screen, cur_dec_pos_map=current_decor_position_map)
            drawing.draw_NPC(
                sc=screen, cur_NPC_pos_map=current_NPC_position_map)

            drawing.draw_player_vision(
                sc=screen, cur_player_vis_map=current_player_vision_map)
            drawing.fps_drawing(clock)

            player_on_stages = Player.movement(
                matrix_walls_map,
                matrix_decor_position_map,
                matrix_NPC_position_map)
            if player_on_stages:
                current_screen = "end_of_game"
                player_on_stages = False
                (Player.x, Player.y) = default_first_level_position
                return (current_screen)
            player_position = (Player.x, Player.y)

        if current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            return (current_screen)
        if (Player.x > 5 or Player.y > 5):
            health_bar.draw(screen)
            damage_bar.draw(screen)
            vision_distance_bar.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def generate_exit(current_screen):
    screen.fill(BLACK)
    pygame.display.set_caption('Выход')
    screen.blit(background_image_to_exit_game, (0, 0))
    running_exit = True
    while running_exit:
        screen.blit(background_image_to_exit_game, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_exit = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_exit_button.is_hovered = back_exit_button.position.collidepoint(
                    pos)
                real_exit_button.is_hovered = real_exit_button.position.collidepoint(
                    pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "exit":
                    if back_exit_button.check_click(event.pos):
                        current_screen = "menu"
                        return (current_screen)
                    elif real_exit_button.check_click(event.pos):
                        pygame.quit()
        if current_screen == "exit":
            pygame.display.set_caption('Подтверждение выхода')
            print_text(
                'Вы уверены, что хотите выйти из игры?',
                50,
                200,
                font_color=WHITE,
                font_type=pygame.font.Font(
                    'fonts/AlgerianBasD [Rus by me] Regular.otf',
                    32))
            back_exit_button.draw(screen)
            real_exit_button.draw(screen)
        elif current_screen == "menu":
            generate_menu(current_screen="menu")
        pygame.display.flip()


def generate_end_of_game(current_screen):
    screen.fill(BLACK)
    pygame.display.set_caption('Выход')
    screen.blit(background_image_to_generate_end_of_game, (0, 0))
    running_exit = True

    while running_exit:
        screen.blit(background_image_to_generate_end_of_game, (0, 0))

        background_field = pygame.Surface((900, 260))  # the size of your rect
        background_field.fill((88, 179, 125))
        background_field.set_alpha(128)  # alpha level
        screen.blit(background_field, (50, 340))
        pygame.display.flip()
        '''
        def generate_gradient(from_color, to_color, height, width):
            channels = []
            for channel in range(3):
                from_value, to_value = from_color[channel], to_color[channel]
                channels.append(
                    np.tile(
                        np.linspace(from_value, to_value, width), [height, 1],
                    ),
                )
            return np.dstack(channels)

        gradient = generate_gradient((63, 95, 127), (195, 195, 255), 1024, 600)
        so = pygame.surfarray.blit_array(
            background_field,
            pygame.surfarray.map_array(background_field, gradient),
        )
        screen.blit(so, (50, 340))
        '''
        font = pygame.font.Font('fonts/Mediteran.ttf', 78)
        # '''
        text_introduction = ["Поздравляем!", "Вы прошли игру!"]
        movement = 0
        for i in text_introduction:
            text_surf_1 = font.render(i, True, WHITE)
            screen.blit(text_surf_1, (75, 360 + movement))
            movement += 120
        pygame.display.flip()
        pygame.time.wait(10000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_exit = False
            if event.type == pygame.MOUSEMOTION:
                current_screen = "main"
                pygame.quit()
        if current_screen == "exit":
            pygame.display.set_caption('Подтверждение выхода')
            print_text(
                'Вы уверены, что хотите выйти из игры?',
                50,
                200,
                font_color=WHITE,
                font_type=pygame.font.Font(
                    'fonts/AlgerianBasD [Rus by me] Regular.otf',
                    32))
            back_exit_button.draw(screen)
            real_exit_button.draw(screen)
        elif current_screen == "menu":
            generate_menu(current_screen="menu")
        pygame.display.flip()
# Функции всплывающих окон


def generate_pause(current_screen):
    pygame.display.set_caption('Пауза')
    screen.blit(background_image_to_pause, (0, 0))
    pygame.display.flip()
    paused = True
    while paused:
        screen.blit(background_image_to_pause, (0, 0))
        print_text(
            message="Пауза",
            x=training_text_location_x - 60,
            y=training_text_location_y - 25,
            font_color=WHITE)
        # print_text("также продолжить игру можно зажав  ESCAPE", 450, 600, font_color=WHITE, font_type= pygame.font.Font('fonts/AlgerianBasD [Rus by me] Regular.otf', 18))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                paused = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                magic_book_button.is_hovered = magic_book_button.position.collidepoint(
                    pos)
                quests_button.is_hovered = quests_button.position.collidepoint(
                    pos)
                equipment_button.is_hovered = equipment_button.position.collidepoint(
                    pos)
                back_to_level_button.is_hovered = back_to_level_button.position.collidepoint(
                    pos)
                exit_button_2.is_hovered = exit_button_2.position.collidepoint(
                    pos)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "pause":
                    if magic_book_button.check_click(event.pos):
                        current_screen = generate_magic_book(
                            cards_compilation=all_cards, current_screen="magic_book")
                    if quests_button.check_click(event.pos):
                        current_screen = generate_quests(
                            current_screen="quests")

                    if equipment_button.check_click(event.pos):
                        current_screen = generate_equipment(
                            current_screen="equipment")
                    if exit_button_2.check_click(event.pos):
                        current_screen = "main"
                        return (current_screen)
                    elif back_to_level_button.check_click(event.pos):
                        current_screen = "training"
                        return (current_screen)


        if current_screen == "pause":
            magic_book_button.draw(screen)
            quests_button.draw(screen)
            equipment_button.draw(screen)
            back_to_level_button.draw(screen)

            exit_button_2.draw(screen)
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen="training")
        elif current_screen == "magic_book":
            pygame.display.set_caption('Книга заклинаний')
            generate_magic_book(
                cards_compilation=all_cards,
                current_screen="magic_book")

        elif current_screen == "equipment":
            pygame.display.set_caption('Инвентарь')
            generate_equipment(current_screen="equipment")
        pygame.display.flip()

    pygame.display.set_caption('First level')
    pygame.display.update()


def generate_magic_book(cards_compilation, current_screen):
    pygame.display.set_caption('Книга заклинаний')
    current_screen = "magic_book"
    spells_book_generating = True
    while spells_book_generating:
        screen.blit(background_image_to_magic_book, (-100, 0))
        print_text(
            message="Гримуар",
            x=training_text_location_x - 60,
            y=training_text_location_y - 25,
            font_color=WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spells_book_generating = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                activate_card_button_1.is_hovered = activate_card_button_1.position.collidepoint(
                    pos)
                activate_card_button_2.is_hovered = activate_card_button_2.position.collidepoint(
                    pos)
                activate_card_button_3.is_hovered = activate_card_button_3.position.collidepoint(
                    pos)
                activate_card_button_4.is_hovered = activate_card_button_4.position.collidepoint(
                    pos)
                activate_card_button_5.is_hovered = activate_card_button_5.position.collidepoint(
                    pos)
                activate_card_button_6.is_hovered = activate_card_button_6.position.collidepoint(
                    pos)
                activate_card_button_7.is_hovered = activate_card_button_7.position.collidepoint(
                    pos)
                activate_card_button_8.is_hovered = activate_card_button_8.position.collidepoint(
                    pos)
                activate_card_button_9.is_hovered = activate_card_button_9.position.collidepoint(
                    pos)
                activate_card_button_10.is_hovered = activate_card_button_10.position.collidepoint(
                    pos)
                back_button2.is_hovered = back_button2.position.collidepoint(
                    pos)
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
                        current_screen = "pause"
                        return (current_screen)

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

    # for i in cards_compilation:
    #    if i.active == 1:


def generate_equipment(current_screen):
    screen.blit(background_image_to_equipment, (0, 0))


    equipment_oppened = True
    while equipment_oppened:

        screen.blit(background_image_to_equipment, (0, 0))
        print_text(
            message="Сумка",
            x=training_text_location_x - 60,
            y=training_text_location_y - 25,
            font_color=WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                equipment_oppened = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(
                    pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "equipment":
                    if back_button2.check_click(event.pos):
                        current_screen = "pause"
                        return (current_screen)

        if current_screen == "equipment":
            back_button2.draw(screen)

        pygame.display.flip()


def generate_quests(current_screen):
    screen.blit(background_image_to_quests, (0, 0))
    quests_table = True
    while quests_table:
        screen.blit(background_image_to_quests, (0, 0))
        print_text(
            message="Квесты",
            x=training_text_location_x - 60,
            y=training_text_location_y - 25,
            font_color=WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quests_table = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(
                    pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "quests":
                    if back_button2.check_click(event.pos):
                        current_screen = "pause"
                        return (current_screen)

        if current_screen == "quests":
            back_button2.draw(screen)

        pygame.display.flip()


# Функции взаимодействия с уже созданнными слоями слоями


def update_major_level_layers(
        last_player_pos,
        player_position,
        matrix_walls_map,
        matrix_player_vision_map,
        vis_distance):

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
    # создаём стек используемых для прорисовки квадратиков стен точек
    matrix_wal_map = matrix_walls_map
    cur_matrix_wal_map = matrix_wal_map
    cur_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_map.add((i * TILE, j * TILE))

    # vis
    # слой с отображением зрения игрока
    # используем основную матрицу
    matrix_player_vis_map = matrix_player_vision_map
    matrix_player_vis_map[last_player_pos] = 1

    matrix_player_vis_map[(player_position[0] -
                           vis_distance):(player_position[0] +
                                          vis_distance +
                                          1), (player_position[1] -
                                               vis_distance): (player_position[1] +
                                                               vis_distance +
                                                               1):] = 0
    matrix_player_vis_map[(player_position[0] -
                           1):(player_position[0] +
                               1 +
                               1), (player_position[1] -
                                    1): (player_position[1] +
                                         1 +
                                         1):] = 0
    matrix_player_vis_map[(player_position[0] -
                           2):(player_position[0] +
                               2 +
                               1), (player_position[1] -
                                    2): (player_position[1] +
                                         2 +
                                         1):] = 0
    # print(matrix_player_vis_map)
    last_player_pos = player_position
    # print(matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))
    return (
        cur_map,
        cur_player_map,
        cur_player_vis_map,
        matrix_player_pos_map,
        matrix_wal_map,
        matrix_player_vis_map)



def update_NPC_level_layer(matrix_NPC_position_map_in_update_NPC_level_layers=np.zeros((48, 32))):
    #matrix_NPC_position_map_in_update_NPC_level_layers = np.ones((48, 32))

    #print("Player.x = ", Player.x, ", Player.y = ", Player.y)
    print("matrix_NPC_position_map_in_update_NPC_level_layers type = ",type(matrix_NPC_position_map_in_update_NPC_level_layers))
    print("matrix_NPC_position_map_in_update_NPC_level_layers size = ", len(matrix_NPC_position_map_in_update_NPC_level_layers))


    #по сторонам света
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x ][Player.y -1] = 0
    #print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x - 1 -1][Player.y -1] = 0
    #print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x -1][Player.y ] = 0
    #print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x - 1][Player.y - 1 -1] = 0
    # по диагонали
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x ][Player.y -1] = 0
    # print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x - 2][Player.y-2] = 0
    # print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x-2][Player.y ] = 0
    # print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    matrix_NPC_position_map_in_update_NPC_level_layers[Player.x][Player.y - 1 -1] = 0
    #print(*matrix_NPC_position_map_in_update_NPC_level_layers)
    # создаём стек используемых для прорисовки позиции NPC точек

    cur_NPC_pos_on_map = matrix_NPC_position_map_in_update_NPC_level_layers
    cur_NPC_pos_map = set()
    set_NPC_coordinates = set()
    for j, row in enumerate(cur_NPC_pos_on_map):
        for i, number in enumerate(row):
            if number == 8:
                cur_NPC_pos_map.add((i * TILE, j * TILE))
                set_NPC_coordinates.add((i, j))
    global buffer_cur_NPC_pos_map
    buffer_cur_NPC_pos_map = cur_NPC_pos_map
    global buffer_matrix_NPC_pos_map
    buffer_matrix_NPC_pos_map = matrix_NPC_position_map_in_update_NPC_level_layers



drawing = Drawing(screen, screen_map)

clock = pygame.time.Clock()

# переключиться в полноэкранный режим
# pygame.display.toggle_fullscreen ()

Player = hero_initialization()
all_cards = cards_initialization()
(health_bar, damage_bar, vision_distance_bar) = status_bar_initialization()

game = True
while game:
    current_screen = choose_window_generation(current_screen)
pygame.quit()
quit()
