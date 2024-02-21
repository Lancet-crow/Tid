import pygame

from time_anomaly import web_generation, update_lines
from making_resources import load_image


def level(screen, clock, fps, level_id):
    FINISH_LEVEL_TIMER = pygame.USEREVENT + 2
    WIDTH, HEIGHT = screen.get_size()
    fon = pygame.transform.scale(load_image(f'level_{str(level_id)}.jpg', screen), (WIDTH, HEIGHT))
    lines = []
    points = []
    web_for_level = {1: 15, 2: 20, 3: 25}
    web_generation(web_for_level[level_id], screen, points, lines)
    moving = False
    moving_object = None
    running = True
    won_game = False
    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
            if event.type == FINISH_LEVEL_TIMER:
                pygame.time.set_timer(FINISH_LEVEL_TIMER, 0)
                return "level_menu"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in points:
                        if (i.pos_x - i.radius < event.pos[0] < i.pos_x + i.radius
                                and i.pos_y - i.radius < event.pos[1] < i.pos_y + i.radius):
                            moving_object = i
                            moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_move, y_move = event.rel
                    moving_object.pos_x += x_move
                    moving_object.pos_y += y_move
                    moving_object.change_color(moving=True)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if moving:
                        moving_object.change_color(moving=False)
                    moving = False
                    moving_object = None
        screen.blit(fon, (0, 0))
        winning_position = update_lines(lines, points)
        if winning_position and not won_game:
            won_game = True
            pygame.time.set_timer(FINISH_LEVEL_TIMER, 5000)
        pygame.display.flip()
        clock.tick(fps)
