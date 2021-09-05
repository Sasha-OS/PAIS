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

# initializing enemy ship
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.projectile_img = None
        self.projectiles = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img , (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = SHIP_RED
        self.projectile_img = RED_PROJECTILE
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

def main():
    run = True
    level = 1
    lives = 3
    kills = 0
    player_speed = 5
    main_font = pygame.font.SysFont("comicsans", 40)
    FPS = 60

    player = Player(300, 650)

    clock = pygame.time.Clock()



    def redraw_window():
        WINDOW.blit(BACKGROUND, (0,0))
        #display info
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 5, 5))
        level_label = main_font.render(f"Level: {level}", 1, (255, 5, 5))
        kills_label = main_font.render(f"Count: {kills}", 1, (255, 5, 5))

        WINDOW.blit(level_label, (10, 10))
        WINDOW.blit(kills_label, (10, 50))
        WINDOW.blit(lives_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(WINDOW)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #moving
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_speed > 0: #left
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + 50 < WIDTH: #right
            player.x += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0: #up
            player.y -= player_speed
        if keys[pygame.K_s] and player.y + player_speed + 50 < HEIGHT: #down
            player.y += player_speed

main()