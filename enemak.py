import os
import random

import pygame as pg

original_image = pg.image.load(os.path.join("./images", "van.png"))
image = pg.transform.scale(original_image, (50, 100))


class Enemka:
    def __init__(self, okenko):
        self.x = random.randrange(1, 4)
        self.y = 0
        self.platno = okenko

    def pohyb(self):
        self.y += 5

    def draw(self):
        self.platno.blit(image, (self.x * 250 - 50, self.y))
