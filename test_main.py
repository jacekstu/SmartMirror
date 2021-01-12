import pygame
import sys
from weather_info import *
from settings import *

pygame.init()
clock = pygame.time.Clock()

#screen = pygame.display.set_mode((600,600))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

running = True

w_obj_1 = WeatherInfo("Warszawa", 10,10) 
w_obj_2 = WeatherInfo("Cancun", 300,10) 
w_obj_3 = WeatherInfo("Cairo", 10,330 ) 
w_obj_3 = WeatherInfo("Belfast", 300,330 ) 

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

    for s in sprite_group:
        screen.blit(s.render_city()[0], s.render_city()[1])
        screen.blit(s.render_date()[0], s.render_date()[1])
        screen.blit(s.render_wind()[0], s.render_wind()[1])
        screen.blit(s.render_temp()[0], s.render_temp()[1])
        screen.blit(s.render_desc()[0], s.render_desc()[1])
        screen.blit(s.render_sunrise()[0], s.render_sunrise()[1])
        screen.blit(s.render_sunset()[0], s.render_sunset()[1])

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
