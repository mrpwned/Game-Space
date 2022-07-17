import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    a = 0
    pygame.init()
    screen = pygame.display.set_mode((650, 750))
    pygame.display.set_caption("Game Space")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemy = Group()
    stats = Stats()
    scores = Scores(screen, stats)

    while True:
        a += 1
        controls.events(screen, gun, bullets)
        if stats.run_game:
            if a == 600:
                controls.enemiess(screen, enemy)
                a -= 600
            gun.update_gun()
            enemy.update()
            controls.update(bg_color, screen, stats, scores, gun, enemy, bullets)
            controls.update_bullets(bullets, stats, scores, enemy)
            controls.enemeis_damage(stats, screen, scores, gun, enemy, bullets)


run()
