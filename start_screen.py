from os import path

import pygame

from general_methods_for_screens import terminate
from making_resources import load_image


class StartScreen:
    def __init__(self, screen, clock, fps):
        BG_ANIMATE_TIMER = pygame.USEREVENT + 1
        item_bg = 0
        a = 1
        self.screen = screen
        pygame.time.set_timer(BG_ANIMATE_TIMER, 1000)
        WIDTH, HEIGHT = self.screen.get_size()
        running = True
        fon = pygame.transform.scale(load_image('start_screen_background_0.png', self.screen), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        self.text_blit()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    from level_menu import LevelMenu
                    LevelMenu(screen, clock, fps)
                elif event.type == BG_ANIMATE_TIMER:
                    if item_bg == 11 and a == 1:
                        pygame.time.set_timer(BG_ANIMATE_TIMER, 0)
                        a = -1
                        pygame.time.set_timer(BG_ANIMATE_TIMER, 700)
                    elif item_bg == 1 and a == -1:
                        pygame.time.set_timer(BG_ANIMATE_TIMER, 0)
                        a = 1
                        pygame.time.set_timer(BG_ANIMATE_TIMER, 700)
                    else:
                        item_bg += a
                        self.bg_blit(item_bg, WIDTH, HEIGHT)
                        self.text_blit()
            pygame.display.flip()
            clock.tick(fps)
        terminate()

    def bg_blit(self, item_bg, WIDTH, HEIGHT):
        fon = pygame.transform.scale(load_image(f'start_screen_background_{item_bg}.png', self.screen), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

    def text_blit(self):
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
            self.screen.blit(string_rendered, intro_rect)
