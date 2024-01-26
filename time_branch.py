import random

import pygame


class DragOperator:
    def __init__(self, sprite):
        self.sprite = sprite
        self.dragging = False
        self.rel_pos = (0, 0)

    def update(self, event_list):
        self.mouse_coordinates = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mouse_coordinates):
            self.rect.centerx = self.mouse_coordinates[0]
            self.rect.centery = self.mouse_coordinates[1]



class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.x, self.y = x, y
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, 50)


class Line(pygame.sprite.Sprite):
    def __init__(self, p1, p2):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.set_colorkey((0, 0, 0))
        self.p1, self.p2 = p1, p2
        self.rect = self.image.get_rect()
        self.drag = DragOperator(self)

    def update(self, event_list):
        self.mouse_coordinates = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mouse_coordinates):
            self.rect.centerx = self.mouse_coordinates[0]
            self.rect.centery = self.mouse_coordinates[1]

        pygame.draw.line(self.image, (255, 255, 255), self.p1.rect.center, self.p2.rect.center, 20)


class LevelBranches:
    def __init__(self, points):
        points_list = []
        self.lines_list = []
        for i in range(points):
            points_list.append(Point(random.randrange(100, 1900), random.randrange(100, 1000)))
        for i in range(len(points_list)):
            self.lines_list.append(Line(points_list[i], points_list[i + 1 if i + 1 < len(points_list) else 0]))

    def get_lines(self):
        return self.lines_list
