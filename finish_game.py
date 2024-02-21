from os import path

import pygame

import music_player


def finish_screen(screen, clock, fps):
    END_MUSIC_TIMER = pygame.USEREVENT + 3
    running = True
    end_timer_working = False
    texts = text_blit(screen)
    screen_rect = screen.get_rect()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == END_MUSIC_TIMER:
                music_player.quit_game_fix()
                return
        screen.fill((0, 0, 0))
        for r, s in texts:
            r.move_ip(0, -1)
            screen.blit(s, r)
        if not screen_rect.collidelistall([r for (r, _) in texts]) and not end_timer_working:
            pygame.time.set_timer(END_MUSIC_TIMER, 3000)
            end_timer_working = True
            pygame.mixer.music.fadeout(3000)
        pygame.display.flip()
        clock.tick(fps)


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
