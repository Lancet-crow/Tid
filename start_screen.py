import sys
from os import path

import pygame

from Tid.load_resources import load_image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, clock, fps):
    WIDTH, HEIGHT = screen.get_size()
    intro_text = ["Правила игры",
                  "1) Работать с нитями аккуратно.",
                  "2) Использовать хронокостюм",
                  "только при крайней необходимости."]

    fon = pygame.transform.scale(load_image('start_screen_background.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(path.join("data", "fonts", "Inter-ExtraBold.ttf"), 30)
    text_coord = 800
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 1300
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)
