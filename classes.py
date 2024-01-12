import pygame
from game_settings import *
pygame.init()


def print_text( message, x, y, font_color, font_type= pygame.font.Font('Mediteran.ttf', 12), sc =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)):
    text_font_type = font_type
    text = text_font_type.render(message, True, font_color)
    sc.blit(text, (x, y))

def define_distance_between_2_positions(position_number_one, position_number_two):
    x1, y1 = position_number_one
    x2, y2 = position_number_two
    delta_x = math.fabs(x1 - x2)
    delta_y = math.fabs(y1 - y2)
    return(max(delta_x, delta_y))
def enemy_initialization(name, healthpoints, damage, armor, attack_range,movement_speed, vision_distance, enemy_position):
    enemy = Enemy(name=players_nick,
                  healthpoints=25,
                  damage=10,
                  armor=0,
                  attack_range=1,
                  movement_speed=1,
                  vision_distance=3,
                  enemy_pos=enemy_position)
    return (enemy)
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
        self.is_alive = True

    def movement(self, current_walls_map, current_decor_map, current_NPC_map):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # north
            if (current_walls_map[self.x - 1][self.y]==0 or current_walls_map[self.x - 1][self.y]==9) and current_NPC_map[self.x - 1][self.y]==0 and current_decor_map[self.x - 1][self.y]==0:
                self.x += -1
                self.y += 0


        elif keys[pygame.K_s]:  # south
            if (current_walls_map[self.x + 1][self.y]==0 or current_walls_map[self.x + 1][self.y]== 9) and current_NPC_map[self.x + 1][self.y]==0 and current_decor_map[self.x + 1][self.y]==0:
                self.x += 1
                self.y += 0

        elif keys[pygame.K_a]:  # west
            if (current_walls_map[self.x][self.y - 1]==0 or current_walls_map[self.x][self.y - 1]==9) and current_NPC_map[self.x][self.y - 1]==0 and current_decor_map[self.x][self.y - 1]==0:
                self.x += 0
                self.y += -1

        elif keys[pygame.K_d]:  # east
            if (current_walls_map[self.x][self.y + 1]==0 or current_walls_map[self.x][self.y + 1]==9)and current_NPC_map[self.x][self.y + 1]==0 and current_decor_map[self.x][self.y + 1]==0:
                self.x += 0
                self.y += 1
        if current_walls_map[self.x][self.y] == 9:
            player_on_stages= True
        else:
            player_on_stages = False
        return(player_on_stages)
        #print(self.x, self.y)
    def fight(self, any_NPC_position, enemies):
        def attack(self, enemy):
            hit = self.damage
            enemy.take_damage(hit)
        dict_of_NPC = {(17, 17): ("NPC_name", 20, 20, 20, 20, 20, 20, (17, 17))}
        enemies=[]
        for NPC_position in any_NPC_position:
            enemies.append(enemy_initialization(*dict_of_NPC[NPC_position]))
        temp = 0
        for element  in enemies:
            print(element)
            distance_to_NPC = define_distance_between_2_positions(position_number_one= (self.x, self.y), position_number_two=(element.x, element.y))
            if distance_to_NPC <= 1.0:
                attack(self, enemy = element)
            temp+=1


    def take(self, any_gold_position):
        #if (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]) or (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]):
            # all gold and medallions that are in surrounding square puts into backpack
            pass

    def take_damage(self, hit):
        injury = hit
        if injury > 0:
            self.healthpoints -= injury
            if self.healthpoints <= 0:
                self.is_alive = False
                self.healthpoints = 0
        print('unit_HP = ', self.healthpoints)

    def is_alive(self):
        return(self.is_alive)
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

class Enemy:
    def __init__(self, name, healthpoints, damage, armor, attack_range, movement_speed, vision_distance, enemy_pos):
        self.name = name
        self.x, self.y = enemy_pos
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

    def fight(self, any_NPC_position):
        for NPC_position in any_NPC_position:
            distance_to_NPC = define_distance_between_2_positions(position_number_one=(self.x, self.y),
                                                                  position_number_two=NPC_position)
            if distance_to_NPC <= 1:
                hero = dict_of_NPC(NPC_position)
                attack(self, hero)

    def attack(self, hero):
        hit = self.damage
        hero.take_damage(hit)

    def take(self, any_gold_position):
        # if (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]) or (player_position[0] + 1 == any_gold_position[0]) or (player_position[0] - 1 == any_gold_position[0]):
        # all gold and medallions that are in surrounding square puts into backpack
        pass

    def take_damage(self, hit):
        injury = hit
        if injury > 0:
            self.healthpoints -= injury
            if self.healthpoints <= 0:
                self.is_alive = False
                print("Убит")
                self.healthpoints = 0
        print('unit_HP = ', self.healthpoints)
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
        self.font = pygame.font.Font('Mediteran.ttf', 26)
        self.width, self.height = 200, 60
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
        pygame.draw.rect(screen, color=(BACKGROUND_STATUS_BAR_COLOR),rect=(self.x, self.y, self.width, self.height))

        # Рассчитываем ширину ползунка в зависимости от значений
        range = self.max_value - self.min_value
        value_offset = self.current_value - self.min_value
        slider_width = int((value_offset / range) * self.width)

        # Отрисовываем ползунок статус бара
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, slider_width, self.height))

        # Отрисовка текста
        print_text(message=self.text, x = self.x, y = self.y, font_color = STATUS_BAR_TEXT_COLOR, font_type =pygame.font.Font('RAINFALL Black.otf', 12))
    def update_value(self, new_value):
        # Обновляем текущее значение статус бара
        self.current_value = new_value



