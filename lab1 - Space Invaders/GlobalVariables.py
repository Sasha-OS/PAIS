import pygame
import os
import time
import random
import ShipClass as SC
import ProjectileClass

OS_LIB = os
PG_LIB = pygame
TIME_LIB = time
RANDOM_LIB = random
ShipClass = SC
ProjectileClass = ProjectileClass

WIDTH, HEIGHT = 750, 750
kills = 0
lost_count = 0
level = 0
lives = 3
player_speed = 5
enemy_speed = 1
projectile_speed = 3
FPS = 60
enemies = []
wave_length = 5

PG_LIB.font.init()
main_font = pygame.font.SysFont("comicsans", 40)
lost_font = pygame.font.SysFont("comicsans", 60)

WINDOW = PG_LIB.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

SHIP_RED = pygame.image.load(os.path.join("assets", "ship_red.png"))
SHIP_BLUE = pygame.image.load(os.path.join("assets", "ship_blue.png"))
SHIP_YELLOW = pygame.image.load(os.path.join("assets", "ship_yellow.png"))
SHIP_GREEN = pygame.image.load(os.path.join("assets", "ship_green.png"))
BLUE_PROJECTILE = pygame.image.load(os.path.join("assets", "blue_projectile.png"))
RED_PROJECTILE = pygame.image.load(os.path.join("assets", "red_projectile.png"))
YELLOW_PROJECTILE = pygame.image.load(os.path.join("assets", "yellow_projectile.png"))
GREEN_PROJECTILE = pygame.image.load(os.path.join("assets", "green_projectile.png"))

COLOR_MAP = {
        "red": (SHIP_RED, RED_PROJECTILE),
        "green": (SHIP_GREEN, GREEN_PROJECTILE),
        "blue": (SHIP_BLUE, BLUE_PROJECTILE)
    }

player = SC.Player(300, 650)