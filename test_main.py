import pygame
import sys
from weather_display import *
from weather_info import *
from settings import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))

running = True

w_obj_1 = WeatherInfo("Warszawa",3600, 0,0) 
w_obj_2 = WeatherInfo("Madrid",3600, 250,0) 
w_obj_3 = WeatherInfo("Cairo",3600, 0,150 ) 

sprite_group = pygame.sprite.Group()
sprite_group.add(w_obj_1)
sprite_group.add(w_obj_2)
sprite_group.add(w_obj_3)


while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0,0,0))
    # draw elements
    sprite_group.draw(screen)

    # update elements
    sprite_group.update()

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
