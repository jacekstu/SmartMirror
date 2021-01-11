import pygame
import sys
from weather_display import *
from weather_info import *
from settings import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400,400))

running = True

w_obj_1 = WeatherInfo("Warszawa",3600) 
wd_obj_1 = WeatherDisplay(w_obj_1, 0,0)

sprite_group = pygame.sprite.Group()
sprite_group.add(wd_obj_1)


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
