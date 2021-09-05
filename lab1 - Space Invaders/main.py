import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Receive images

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

SHIP_RED = pygame.image.load(os.path.join("assets", "ship_red.png"))
SHIP_BLUE = pygame.image.load(os.path.join("assets", "ship_blue.png"))
SHIP_YELLOW = pygame.image.load(os.path.join("assets", "ship_yellow.png"))
SHIP_GREEN = pygame.image.load(os.path.join("assets", "ship_green.png"))
BLUE_PROJECTILE = pygame.image.load(os.path.join("assets", "blue_projectile.png"))
RED_PROJECTILE = pygame.image.load(os.path.join("assets", "red_projectile.png"))
YELLOW_PROJECTILE = pygame.image.load(os.path.join("assets", "yellow_projectile.png"))
GREEN_PROJECTILE = pygame.image.load(os.path.join("assets", "green_projectile.png"))


def main():
    run = True
    level = 1
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 40)
    FPS = 60
    clock = pygame.time.Clock()



    def redraw_window():
        WINDOW.blit(BACKGROUND, (0,0))
        #display info
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 5, 5))
        level_label = main_font.render(f"Level: {level}", 1, (255, 5, 5))

        WINDOW.blit(level_label, (10, 10))
        WINDOW.blit(lives_label, (WIDTH - level_label.get_width() - 10, 10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()