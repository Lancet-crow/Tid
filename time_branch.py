import math
from random import randrange

import pygame

from making_resources import load_image


class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def update(self):
        vec = round(math.cos(self.angle * math.pi / 180) * 100), round(math.sin(self.angle * math.pi / 180) * 100)
        self.angle = (self.angle + 1) % 360
        self.image.fill(0)
        pygame.draw.line(self.image, (223, 171, 255), (100 - vec[0], 100 - vec[1]), (100 + vec[0], 100 + vec[1]), 5)
        self.mask = pygame.mask.from_surface(self.image)


class MainBranch(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = load_image("main_branch.png", screen)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)


class Branch(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = load_image("good_branch.png", screen)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y + randrange(-50, 50)

    def colliding_other(self, group):
        return any(self.rect.colliderect(branch.rect) for branch in group if self != branch)

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)

    def rewriting_to_bad(self):
        self.image = load_image("bad_branch.png", self.screen)
