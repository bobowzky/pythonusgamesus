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
    time = 0
    auto = auticko.Auticko(okenko)
    enemy = enemak.Enemka(okenko)
    while running:
        time+=1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    auto.pohyb("do_prava")
                if event.key == pg.K_a:
                    auto.pohyb("do_leva")
        okenko.fill((0,200,0))


        road.draw_road(okenko, time)
        auto.draw()
        enemy.pohyb()
        enemy.draw()




        pg.display.flip()
        clock.tick(60)
main()
