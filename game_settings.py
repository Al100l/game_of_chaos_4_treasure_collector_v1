import pygame
import math
pygame.init()

#game settings

SCREEN_WIDTH        =   1200
SCREEN_HEIGHT       =   800
SCREEN_HALF_WIDTH   =   SCREEN_WIDTH   // 2
SCREEN_HALF_HEIGHT  =   SCREEN_HEIGHT  // 2

map_width = SCREEN_WIDTH // 25
map_height = SCREEN_HEIGHT // 25

#player settings
players_nick = "Ренион"

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

#ray_casting
SCALE = SCREEN_WIDTH // NUM_RAYS_IN_FIELD_OF_VIEW


# FPS settings
FPS_POSITION =(SCREEN_WIDTH - 65, 5)

#background images
background_image_to_magic_book = pygame.image.load("magic_book.jpg")
background_image_to_start_screen = pygame.image.load("main_page.jpeg")
background_image_to_pause = pygame.image.load("pause.jpg")
background_image_to_training_level = pygame.image.load("training_level.jpg")
background_image_to_about_game = pygame.image.load("about_game.jpg")
background_image_to_exit_game = pygame.image.load("exit_game.jpeg")
background_image_to_equipment = pygame.image.load("equipment.jpg")
background_image_to_quests = pygame.image.load("quests.jpg")
#screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

screen_map = pygame.Surface((SCREEN_WIDTH // MAP_SCALE, SCREEN_HEIGHT//MAP_SCALE))

pygame.display.set_caption('Начальный экран')

pygame.display.set_icon(pygame.image.load('icon.jpg'))

current_screen ="main"

#text
training_text_location_x= 640

training_text_location_y= 35


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

DARK_PURPLE = (66, 25, 84)

DARK_BLUE =(34, 93, 92)

STATUS_BAR_TEXT_COLOR = (149, 204, 191)

BACKGROUND_STATUS_BAR_COLOR = ( 57, 98, 112)

STATUS_BAR_HP_BACKGROUND_COLOR = (87, 21, 39)

STATUS_BAR_DAMAGE_BACKGROUND_COLOR = (21, 72, 87)

STATUS_BAR_VISION_BACKGROUND_COLOR = (21, 87, 53)
