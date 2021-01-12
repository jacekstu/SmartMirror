import pygame
import os
pygame.init()

DEGREE_SIGN = u"\N{DEGREE SIGN}"
API_KEY = os.environ.get('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="

font0 = pygame.font.SysFont(None, 30)
font1 = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 32)
font3 = pygame.font.SysFont(None, 100)

def load_img(path, res):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, res)
    return img



WHITE = (255,255,255)
BLACK = (0,0,9)

THUNDER_LT = []
for i in range(1,7):
    THUNDER_LT.append(load_img("assets/" + str(i) + ".png", (100,100)))

SNOWING_LT = []
for i in range(1,10):
    SNOWING_LT.append(load_img("assets/" + str(i) + "a.png", (100,100)))


countries_dt = {

    "PL":"Poland",
    "DE":"Germany",
    "ES":"Spain",
    "EG":"Egypt",
    "MX":"Mexico",
    "GB":"Great Britain",
    "FR":"France"

        }
