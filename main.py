import pygame

SIZE = [400, 600]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()