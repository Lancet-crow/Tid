import pygame

import music_player
from general_methods_for_screens import terminate

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
running = True
scene = "start_screen"

music_player.load_level_music('main')

# time_changer = Chronosuit()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if scene == "start_screen":
        from start_screen import start_screen
        scene = start_screen(screen, clock, FPS)
    elif scene == "level_menu":
        from level_menu import level_menu
        scene = level_menu(screen, clock, FPS)
    elif scene == "level_1":
        from level_1 import level_one
        scene = level_one(screen, clock, FPS)
    elif scene == "level_2":
        from level_2 import level_two
        scene = level_two(screen, clock, FPS)
    elif scene == "level_2":
        from level_3 import level_three
        scene = level_three(screen, clock, FPS)
    pygame.display.flip()
    clock.tick(FPS)
music_player.quit_game_fix()
terminate()
