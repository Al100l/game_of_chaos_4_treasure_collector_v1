from game_settings import *
import pygame
import math

class Player :
    def __init__(self) :
        self.x, self.y = player_position
        self.angle = player_angle
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]: #north
            self.x +=   player_speed * cos_a
            self.y +=   player_speed * sin_a
            #self.y = self.y - player_speed
        if keys[pygame.K_s]: #south
            self.x +=  - player_speed * cos_a
            self.y +=  - player_speed * sin_a
            #self.y = self.y + player_speed
        if keys[pygame.K_a]: #east
            self.x +=   player_speed * sin_a
            self.y += - player_speed * cos_a
            #self.x = self.x - player_speed
        if keys[pygame.K_d]: #west
            self.x += - player_speed * sin_a
            self.y +=   player_speed * cos_a
            #self.x = self.x + player_speed
        if keys[pygame.K_LEFT]: #Left_rotation
            self.angle = self.angle - 0.2
        if keys[pygame.K_RIGHT]: #right_rotation
            self.angle = self.angle + 0.2
    @property
    def position(self):
        return(self.x, self.y)
