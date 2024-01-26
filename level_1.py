from operator import attrgetter

import pygame

from general_methods_for_screens import terminate
from making_resources import load_image
import time_branch


class LevelOne:
    def __init__(self, screen, clock, fps):
        WIDTH, HEIGHT = screen.get_size()
        running = True
        self.screen = screen
        fon = pygame.transform.scale(load_image('level_1.jpg', self.screen), (WIDTH, HEIGHT))
        # moving_object = SpriteObject(0, 0, load_image("button_sprite_level_3.png", screen).convert_alpha())
        # line_object = Line(*screen.get_rect().center)
        all_branches = pygame.sprite.Group(*time_branch.LevelBranches(5).get_lines())
        while running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    sprites = []
                    for sprite in all_branches:
                        if sprite.rect.collidepoint(event.pos):
                            sprites.append(sprite)
                    try:
                        active = min(sprites, key=attrgetter('rect'))
                    except ValueError:
                        active = None
                        print('Empty place selected, so sprite list is empty')
                    mouse_held = True
                    if mouse_held:
                        try:
                            active.update(event_list)
                        except UnboundLocalError:
                            print(
                                'active not set, to due to previous exception')
            all_branches.update(event_list)
            # for branch in good_branches:
            #     if branch.colliding_other(good_branches):
            #         bad_branches.add(branch)
            #         good_branches.remove(branch)
            #         branch.rewriting_to_bad()

            self.screen.blit(fon, (0, 0))
            all_branches.draw(screen)
            pygame.display.flip()
            clock.tick(fps)
        terminate()
