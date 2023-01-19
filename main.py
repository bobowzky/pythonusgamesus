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
        timespeed+=0.0001
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    auto.pohyb("do_prava")
                if event.key == pg.K_a:
                    auto.pohyb("do_leva")


        if game:
            okenko.fill((0,200,0))
            road.draw_road(okenko, time)
            auto.draw()
            enemy.pohyb(timespeed)
            enemy.draw()
            # Červená barva pro skóre, je zde z důvodu, aby byl Matěj naštván (Na žádost Dana)
            text = font.render('Skóre: '+ str(body), True, (255,0,0))
            okenko.blit(text, (0,0,50,50))
            if enemy.passed():
                enemy = enemak.Enemka(okenko)
                body += 69
            if auto.kolize(enemy):
                game = False
        else:
            okenko.fill((0, 0, 0))
            text = font.render('GAME OVER TVÉ SKÓRE JE: ' + str(body), True, (255, 0, 0))
            textRect = text.get_rect()
            textRect.center = (450, 450)
            okenko.blit(text, textRect)

        pg.display.flip()
        clock.tick(60)
main()
