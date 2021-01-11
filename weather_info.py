import pygame
from datetime import datetime
import requests, json
from settings import *

class WeatherInfo(pygame.sprite.Sprite):
    
    def __init__(self, city, offset, x, y, lang="eng", units="metric"):
        super().__init__()
        # user defined attributes - showing to Filipek
        self.city = city
        self.offset = offset
        self.lang = lang
        self.units = units
        self.url = BASE_URL + self.city + \
            "&units=" + self.units + "&appid=" + API_KEY + \
            "&lang" + self.lang
        self.response = requests.get(self.url)
        self.json_obj = json.loads(self.response.content)

        # attributes obtained by parsing weather API's response
        self.temp = self.get_temp()
        self.weather, self.desc = self.get_weather()
        self.wind_speed, self.wind_dir = self.get_wind()
        self.sunrise, self.sunset = self.sun();

        # attributes needed for displaying on the screen
        self.current_sprite = 0
        self.lt = self.get_sprite_lt()
        self.image = self.lt[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y  = [x,y]

        # other vars
        self.timer = 0

    def update(self):
        # animate the weather image
        self.current_sprite += 0.5
        if self.current_sprite >= len(self.lt):
            self.current_sprite = 0
        self.image = self.lt[int(self.current_sprite)]

        # update weather information every minute
        if self.timer >= 3000:
            self.response = requests.get(self.url)
            self.json_obj = json.loads(self.response.content)
            self.timer = 0
            print(self.wind_speed)

        self.timer += 1


    def get_sprite_lt(self):
        if self.get_weather()[0] == 'Clear':
            return THUNDER_LT
        else:
            return SNOWING_LT

    def get_temp(self):
        temp_dict = self.json_obj['main']
        temperature = (str(int(temp_dict['temp'])) + DEGREE_SIGN)
        return temperature

    def get_weather(self):
        weather_dict_main = self.json_obj['weather']
        weather_dict_sub = weather_dict_main[0]
        weather = weather_dict_sub['main']
        description = weather_dict_sub['description']
        return weather, description

    def get_wind(self):
        wind_dict_main = self.json_obj['wind']
        wind_speed = wind_dict_main['speed']
        degrees = wind_dict_main['deg']
        wind_dir = self.get_dir(degrees)
        return wind_speed, wind_dir

    def get_dir(self, dg):
        wdir = ''
        if dg > 16 and dg <= 60:
            wdir = 'NE'
        if dg > 60 and dg <= 120:
            wdir = 'E'
        if dg > 120 and dg <= 160:
            wdir = 'SE'
        if dg > 160 and dg <= 210:
            wdir = 'S'
        if dg > 210 and dg <= 240:
            wdir = 'SW'
        if dg > 240 and dg <= 300:
            wdir = 'W'
        if dg > 300 and dg <= 330:
            wdir = 'NW'
        if dg >= 330 and dg <= 360 or dg >= 0 and dg <= 16:
            wdir = 'N'
        return wdir

    def time_convert(self, unix_time):
        ts = int(unix_time) + self.offset
        return datetime.utcfromtimestamp(ts).strftime("%H:%M:%S")


    def sun(self):
        sun_dict = self.json_obj['sys']
        sunrise = self.time_convert(sun_dict['sunrise'])
        sunset = self.time_convert(sun_dict['sunset'])
        return sunrise, sunset

