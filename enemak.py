import os
import random

import pygame as pg

original_image = pg.image.load(os.path.join("./images", "taxi.png"))
image = pg.transform.scale(original_image, (50, 100))


class Enemka:
    def __init__(self, okenko):
        self.x = random.randrange(1, 4)
        self.y = 0
        self.platno = okenko

    def pohyb(self, timespeed):
        self.y += 5*timespeed


    def draw(self):
        self.platno.blit(image, (self.x * 250 - 75, self.y))
    def passed(self):
        if self.y > 900:
            return True
