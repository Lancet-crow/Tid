from math import sqrt

import pygame

pygame.init()

# from main import *

run = True
clocker = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)


class TimeBranch(pygame.sprite.Sprite):
    def __init__(self, pos, x, y):
        pygame.sprite.Sprite.__init__(self)


class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))  # точка 5x5
        self.image.fill((255, 255, 255))  # закрасить черным цветом
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # центр по x
        self.rect.centery = y  # центр по y


def Calc(func):
    i = -10  # начальное значение аргумента
    while i <= 10:  # пока аргумент меньше 10
        mass = ""  # темп-строка
        for j in func:  # для каждого символа в строке func(наша функция)
            if j == "x":  # если символ = x, то добавляем i в темп-строку
                mass += str(i)
            else:  # если нет, то добавить исходный символ
                mass += j
            i += 0.0001  # увеличить аргумент на 0.0001
        try:
            res1 = eval(mass)  # посчитать функцию и получить результат
        except:
            res1 = 10000  # если функцию нельзя посчитать, то результат число вне координат(знаю, костыль)
        dot = Dot(250 + i * 10,
                  250 - res1 * 10)  # dot - точка с координатой(0+x,0+y), так как это дисплей, то вектор "y"
        # направлен вниз
        all_sprites.add(dot)  # добавить точку в группу спрайтов


all_sprites = pygame.sprite.Group()
Calc("y = sqrt(x) ** (4/5)")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen, None)
    pygame.display.flip()
pygame.quit()
