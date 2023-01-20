import pygame as pg
import auticko
import enemak
import road


def main():
    pg.init()
    pg.display.set_caption("Auticka")
    okenko = pg.display.set_mode((900,900))
    clock = pg.time.Clock()
    running = True
    game = True
    time = 0
    auto = auticko.Auticko(okenko)
    enemy = enemak.Enemka(okenko)
    body = 0
    font = pg.font.Font(None, 32)
    font_velky = pg.font.Font(None, 72)
    timespeed = 1

    while running:
        time+=timespeed
        timespeed+=0.001
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    auto.pohyb("do_prava")
                if event.key == pg.K_LEFT:
                    auto.pohyb("do_leva")


        if game:
            okenko.fill((0,200,0))
            road.draw_road(okenko, time)
            auto.draw()
            enemy.pohyb(timespeed)
            enemy.draw()
            text = font.render('Skóre: '+ str(body), True, (255,0,0))
            okenko.blit(text, (0,0,50,50))
            if enemy.passed():
                enemy = enemak.Enemka(okenko)
                body += 69
            if auto.kolize(enemy):
                game = False
        else:
            okenko.fill((0, 0, 0))
            text = font_velky.render('Konec hry', True, (255, 0, 0))
            text2 = font_velky.render('Skóre: ' + str(body), True, (255, 0, 0))
            text3 = font_velky.render('Pro pokračováni stiskni: R', True, (255,0,0))
            textRect = text.get_rect()
            textRect.center = (450, 400)
            text2Rect = text.get_rect()
            text2Rect.center = (470, 450)
            text3Rect = text.get_rect()
            text3Rect.center = (255, 500)
            okenko.blit(text, textRect)
            okenko.blit(text2, text2Rect)
            okenko.blit(text3, text3Rect)
            if pg.key.get_pressed()[pg.K_r]:
                game = True
                time = 0
                enemy = enemak.Enemka(okenko)
                body = 0
                timespeed = 1

        pg.display.flip()
        clock.tick(60)
main()
