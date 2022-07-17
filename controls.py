import pygame
import sys
import time
from bullet import Bullet
from enemies import Enemy


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, scores, gun, enemy, bullets):
    screen.fill(bg_color)
    scores.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemy.draw(screen)
    pygame.display.flip()


def update_bullets(bullets, stats, scores, enemy):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, enemy, True, True)
    if collections:
        stats.score += 1
    scores.image_scores()
    check_high_score(stats, scores)
    scores.image_guns()


def enemiess(screen, enemy):
    ene = Enemy(screen)
    enemy.add(ene)


def enemeis_damage(stats, screen, scores, gun, enemy, bullets):
    if pygame.sprite.spritecollideany(gun, enemy):
        kill(stats, screen, scores, gun, enemy, bullets)
    enemy_check(stats, screen, scores, gun, enemy, bullets)


def kill(stats, screen, scores, gun, enemy, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        enemy.empty()
        scores.image_guns()
        bullets.empty()
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def enemy_check(stats, screen, scores, gun, enemy, bullets):
    screen_rect = screen.get_rect()
    for ene in enemy.sprites():
        if ene.rect.bottom >= screen_rect.bottom:
            kill(stats, screen, scores, gun, enemy, bullets)
            break


def check_high_score(stats, scores):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scores.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))
