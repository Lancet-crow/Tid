import os
import sys

import pygame


def load_image(name, screen, colorkey=None):
    pygame.init()
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
        image = image.convert_alpha()
    return image


class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, filename, screen, top_left_coords):
        super().__init__()
        self.image = load_image(filename, screen)
        self.rect = self.image.get_rect(topleft=top_left_coords)


class ButtonSprite(CustomSprite):
    def __init__(self, filename, screen, top_left_coords, scene):
        super().__init__(filename, screen, top_left_coords)
        scene.buttons.add(self)
        self.filename = filename
        self.clicked = False

    def update(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = not self.clicked
            print(self.filename, "is pushed!", self.clicked)
        if self.clicked:
            from main import screen, clock, FPS
            if self.filename == "button_sprite_level_1.png":
                from level_1 import LevelOne
                LevelOne(screen, clock, FPS)
