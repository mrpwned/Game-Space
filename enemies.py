import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0(3).png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(55, 580)
        self.rect.y = random.randint(50, 60)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.2
        self.rect.y = self.y
