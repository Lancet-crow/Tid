import pygame

from time_anomaly import web_generation, update_lines
from general_methods_for_screens import terminate
from making_resources import load_image


def level_three(screen, clock, fps):
    WIDTH, HEIGHT = screen.get_size()
    screen = screen
    fon = pygame.transform.scale(load_image('level_3.jpg', screen), (WIDTH, HEIGHT))
    lines = []
    points = []
    web_generation(25, screen, points, lines)
    moving = False
    moving_object = None
    running = True
    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
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
        pygame.display.flip()
        clock.tick(fps)
        if winning_position:
            print("Winning position is found!")
            pygame.time.delay(5000)
            return "level_menu"
    terminate()
