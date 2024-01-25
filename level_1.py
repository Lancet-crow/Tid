import pygame

from general_methods_for_screens import terminate
from making_resources import load_image
from time_branch import Line, SpriteObject, MainBranch, Branch


class LevelOne:
    def __init__(self, screen, clock, fps):
        WIDTH, HEIGHT = screen.get_size()
        running = True
        self.screen = screen
        fon = pygame.transform.scale(load_image('level_1.jpg', self.screen), (WIDTH, HEIGHT))
        # moving_object = SpriteObject(0, 0, load_image("button_sprite_level_3.png", screen).convert_alpha())
        # line_object = Line(*screen.get_rect().center)
        main_branch = MainBranch(*screen.get_rect().center, screen)
        good_branches = pygame.sprite.Group(Branch(*main_branch.image.get_rect().center, screen))
        bad_branches = pygame.sprite.Group()
        all_branches = pygame.sprite.Group(main_branch, good_branches, bad_branches)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_branches.update()
            for branch in good_branches:
                if branch.colliding_other(good_branches):
                    bad_branches.add(branch)
                    good_branches.remove(branch)
                    branch.rewriting_to_bad()

            self.screen.blit(fon, (0, 0))
            all_branches.draw(screen)
            pygame.display.flip()
            clock.tick(fps)
        terminate()
