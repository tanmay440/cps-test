import buttons
import pygame
win = pygame.display.set_mode((700, 700))
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()