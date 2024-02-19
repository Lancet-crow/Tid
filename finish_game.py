from os import path

import pygame

from general_methods_for_screens import terminate
from making_resources import load_image


def finish_screen(screen, clock, fps):
    running = True
    texts = text_blit(screen)
    screen_rect = screen.get_rect()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for r, s in texts:
            r.move_ip(0, -1)
            screen.blit(s, r)
        if not screen_rect.collidelistall([r for (r, _) in texts]):
            return
        pygame.display.flip()
        clock.tick(fps)
    terminate()


def text_blit(screen):
    font = pygame.font.Font(path.join("data", "fonts", "Inter-ExtraBold.ttf"), 50)
    texts = []
    screen_rect = screen.get_rect()
    with open("finish_titles.txt", encoding="utf-8", mode="r") as f:
        for id_line, line in enumerate(f.readlines()):
            s = font.render(line.strip(), 1, (255, 255, 255))
            r = s.get_rect(centerx=screen_rect.centerx, y=screen_rect.bottom + id_line * 45)
            texts.append((r, s))
        f.close()
    return texts
