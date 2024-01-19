import pygame

import music_player
from chronosuit import Chronosuit
import draw_a_game
from start_screen import start_screen

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
running = True


all_sprites = pygame.sprite.Group()
draw_a_game.create_bg()
time_changer = Chronosuit()

music_player.load_level_music('main')

start_screen(screen, clock, FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                time_changer.start_time()
            if event.key == pygame.K_LEFT:
                time_changer.change_time(-1)
            if event.key == pygame.K_RIGHT:
                time_changer.change_time(1)
            if event.key == pygame.K_DOWN:
                time_changer.stop_time()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
music_player.quit_game_fix()
pygame.quit()
