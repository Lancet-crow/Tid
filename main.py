import pygame

import music_player
from general_methods_for_screens import terminate

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
running = True
scene = "start_screen"
passed_levels = []
blocked_levels = [2, 3]

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
        print(scene)
        level_id = int(scene[-1])
        if level_id not in blocked_levels:
            print(level_id not in blocked_levels)
            from level import level
            scene = level(screen, clock, FPS, level_id)
            passed_levels.append(level_id)
            if level_id == 1:
                blocked_levels = [1, 3]
            elif level_id == 2:
                blocked_levels = [1, 2]
            elif level_id == 3:
                blocked_levels = [1, 2, 3]
        else:
            scene = "level_menu"
    if sum(passed_levels) == 6:
        from finish_game import finish_screen
        finish_screen(screen, clock, FPS)
        running = False
    pygame.display.flip()
    clock.tick(FPS)
music_player.quit_game_fix()
terminate()
