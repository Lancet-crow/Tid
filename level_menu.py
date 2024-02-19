import pygame

from general_methods_for_screens import terminate
from making_resources import load_image, ButtonSprite


def level_menu(screen, clock, fps):
    WIDTH, HEIGHT = screen.get_size()
    running = True
    buttons = []
    fon = pygame.transform.scale(load_image('level_menu.png', screen), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    draw_level_buttons(screen, buttons)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # running = False
                for button in buttons:
                    clicked = button.update(event)
                    if clicked is not None:
                        return clicked
        pygame.display.flip()
        clock.tick(fps)
    terminate()


def draw_level_buttons(screen, buttons):
    for i in range(1, 4):
        try:
            screen.blit(ButtonSprite(f"button_sprite_level_{i}.png",
                                     screen, (450 * i, 200), buttons).image, (400 * i, 200))
        except Exception as Exy:
            print(Exy.__repr__())
