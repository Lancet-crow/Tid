import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        try:
            image = image.convert_alpha()
        except Exception as exception:
            print("Can't convert image alpha canals", exception)
    return image


class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        from main import all_sprites
        super().__init__(all_sprites)
        self.image = load_image(filename)
        self.rect = self.image.get_rect()
