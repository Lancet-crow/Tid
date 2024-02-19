import pygame

import music_player
from general_methods_for_screens import terminate

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
running = True
scene = "start_screen"
passed_levels = [6]

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
    elif "level_" in scene:
        from level import level
        scene = level(screen, clock, FPS, int(scene[-1]))
        passed_levels.append(int(scene[-1]))
    if sum(passed_levels) == 6:
        from finish_game import finish_screen
        finish_screen(screen, clock, FPS)
        running = False
    pygame.display.flip()
    clock.tick(FPS)
music_player.quit_game_fix()
terminate()
