import pygame

import music_player
import start_screen
from chronosuit import Chronosuit
from general_methods_for_screens import terminate

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
running = True

music_player.load_level_music('main')

# time_changer = Chronosuit()

start_screen.StartScreen(screen, clock, FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         time_changer.start_time()
        #     if event.key == pygame.K_LEFT:
        #         time_changer.change_time(-1)
        #     if event.key == pygame.K_RIGHT:
        #         time_changer.change_time(1)
        #     if event.key == pygame.K_DOWN:
        #         time_changer.stop_time()
    pygame.display.flip()
    clock.tick(FPS)
music_player.quit_game_fix()
terminate()
