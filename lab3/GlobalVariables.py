import pygame
import os
import time
import random
import ShipClass as SC
import ProjectileClass
import AsteroidClass
import numpy

OS_LIB = os
PG_LIB = pygame
TIME_LIB = time
RANDOM_LIB = random
ShipClass = SC
ProjectileClass = ProjectileClass
AsteroidClass = AsteroidClass

WIDTH, HEIGHT = 750, 750
kills = 0
lost = False
lost_count = 0
level = 0
lives = 3
player_speed = 5
enemy_speed = 1
projectile_speed = 3
FPS = 60
enemies = []
asteroids = []
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
ASTEROID_PICTURE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "asteroid.png")), (30, 30))
PIXELPOINT = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "pixel.png")), (10, 10))
WAY = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "unknown.png")), (15, 15))

COLOR_MAP = {
        "red": (SHIP_RED, RED_PROJECTILE),
        "green": (SHIP_GREEN, GREEN_PROJECTILE),
        "blue": (SHIP_BLUE, BLUE_PROJECTILE)
    }

player = SC.Player(300, 650)

currPoint = [player.x/150, player.y/150]
dfsArrayOfPath = []
bfsArrayOfPath = []
End = False
path = []
VisitMatrix = numpy.full((int(WIDTH / 50), int(HEIGHT / 50)), 0)
findedPoints = []
enemyCount = 0
currAlg = "ucs"
pixelPath = []
work = True