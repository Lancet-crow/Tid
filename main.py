import pygame

from start_screen import start_screen

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
running = True

start_screen(screen, clock, FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()
