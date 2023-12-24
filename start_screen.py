import sys
from os import path

import pygame

from load_resources import load_image


BG_ANIMATE_TIMER = pygame.USEREVENT + 1


def terminate():
    pygame.quit()
    sys.exit()


def bg_blit(screen, item_bg, WIDTH, HEIGHT):
    fon = pygame.transform.scale(load_image(f'start_screen_background_{item_bg}.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))


def text_blit(screen):
    intro_text = ["Правила игры",
                  "1) Работать с нитями аккуратно.",
                  "2) Использовать хронокостюм",
                  "только при крайней необходимости."]
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


def start_screen(screen, clock, fps):
    item_bg = 0
    pygame.time.set_timer(BG_ANIMATE_TIMER, 1000)
    WIDTH, HEIGHT = screen.get_size()
    fon = pygame.transform.scale(load_image('start_screen_background.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text_blit(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
            elif event.type == BG_ANIMATE_TIMER:
                if item_bg == 11:
                    pygame.time.set_timer(BG_ANIMATE_TIMER, 0)
                else:
                    item_bg += 1
                    bg_blit(screen, item_bg, WIDTH, HEIGHT)
                    text_blit(screen)
        pygame.display.flip()
        clock.tick(fps)
