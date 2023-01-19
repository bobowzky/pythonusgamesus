import pygame as pg

SPEED = 2
SPACES = 70
WHITE = (255, 255, 255)


def draw_road(okenko, time):
    y1 = -70
    y2 = -70
    #                               x   y   w   h
    pg.draw.rect(okenko, (100, 100, 100), (50, 0, 800, 900))
    pg.draw.rect(okenko, WHITE, (60, 0, 5, 900))
    pg.draw.rect(okenko, WHITE, (835, 0, 5, 900))
    for i in range(0, 18):
        pg.draw.rect(okenko, WHITE, (300 - 2.5, y1 + SPACES * i + ((time * SPEED) % SPACES), 5, 50))
        pg.draw.rect(okenko, WHITE, (600 - 2.5, y2 + SPACES * i + ((time * SPEED) % SPACES), 5, 50))
