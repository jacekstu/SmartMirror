#class that receives the weather info and pushes it to the main
import pygame
import requests, json
from datetime import datetime
import os
from settings import *
from weather_info import * 

class WeatherDisplay(pygame.sprite.Sprite):

    def __init__(self, weather_inf_obj, x, y):
        super().__init__()
        self.w_obj = weather_inf_obj
        self.lt = self.get_sprite_lt()
        self.current_sprite = 0
        self.image = self.lt[self.current_sprite]
        self.rect = self.image.get_rect()

    def get_sprite_lt(self):
        if self.w_obj == 'Mist':
            return SNOWING_LT
        else:
            return SNOWING_LT

    def update(self):
        pass
