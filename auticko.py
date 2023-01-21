import os

import pygame

original_image = pygame.image.load(os.path.join("./images", "car.png"))
image = pygame.transform.scale(original_image, (50, 100))


class Auticko:

    def __init__(self, okenko):
        self.okenko = okenko
        self.x = 2

    def pohyb(self, smer):
        if smer == "do_prava" and self.x < 3:
            self.x += 1
        elif smer == "do_leva" and self.x > 1:
            self.x -= 1

    def draw(self):
        self.okenko.blit(image, (self.x * 250 - 75, 750))

    def kolize(self, enemak):
        if self.x == enemak.x:
           if 650 < enemak.y and 850 > enemak.y:
               return True

