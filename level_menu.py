import pygame

from general_methods_for_screens import terminate
from making_resources import load_image, ButtonSprite


class LevelMenu:
    def __init__(self, screen, clock, fps):
        WIDTH, HEIGHT = screen.get_size()
        self.screen = screen
        running = True
        self.buttons = pygame.sprite.Group()
        fon = pygame.transform.scale(load_image('level_menu.png', self.screen), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        self.draw_level_buttons()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    self.buttons.update(event)
            pygame.display.flip()
            clock.tick(fps)
        terminate()

    def draw_level_buttons(self):
        for i in range(1, 4):
            try:
                # f"button_sprite_level_{i}.png"
                self.screen.blit(ButtonSprite(f"button_sprite_level_{i}.png",
                                              self.screen, (450 * i, 200), self).image, (400 * i, 200))
            except Exception as Exy:
                print(Exy.__repr__())
