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

#initializing main class projectile
class Projectile:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


    def move(self, speed):
        self.y += speed

    def off_screen(self, height):
        return not(self.y < height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

# initializing main class ship
class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.projectile_img = None
        self.projectiles = []
        self.cool_down_counter = 0

    def move_projectiles(self, speed, obj):
        self.cooldown()
        for projectile in self.projectiles:
            projectile.move(speed)
            if projectile.off_screen(HEIGHT):
                self.projectiles.remove(projectile)
            elif projectile.collision(obj):
                obj.health -= 10
                self.projectiles.remove(projectile)

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for projectile in self.projectiles:
            projectile.draw(window)

    def shoot(self):
        if self.cool_down_counter == 0:
            projectile = Projectile(self.x, self.y, self.projectile_img)
            self.projectiles.append(projectile)
            self.cool_down_counter = 1

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter +=1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = SHIP_YELLOW
        self.projectile_img = YELLOW_PROJECTILE
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_projectiles(self, speed, objs):
        self.cooldown()
        for projectile in self.projectiles:
            projectile.move(speed)
            if projectile.off_screen(HEIGHT):
                self.projectiles.remove(projectile)
            else: #kill enemy
                for obj in objs:
                    if projectile.collision(obj):
                        objs.remove(obj)
                        if projectile in self.projectiles:
                            self.projectiles.remove(projectile)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))


class Enemy(Ship):
    COLOR_MAP = {
        "red": (SHIP_RED, RED_PROJECTILE),
        "green": (SHIP_GREEN, GREEN_PROJECTILE),
        "blue": (SHIP_BLUE, BLUE_PROJECTILE)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.projectile_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move(self, speed):
        self.y += speed

    def shoot(self):
        if self.cool_down_counter == 0:
            projectile = Projectile(self.x-20, self.y, self.projectile_img)
            self.projectiles.append(projectile)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    lost = False
    lost_count = 0
    run = True
    level = 0
    lives = 3
    kills = 0
    player_speed = 5
    enemy_speed = 1
    projectile_speed = 3
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 60)

    FPS = 60

    player = Player(300, 650)
    enemies = []
    wave_length = 5
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
        for enemy in enemies:
            enemy.draw(WINDOW)

        if lost:
            lost_label = lost_font.render("You lost...", 1, (255, 10, 10))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        player.draw(WINDOW)


        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count +=1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            #spawn enemies
            for i in range(wave_length):
                enemy = Enemy(random.randrange(100, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        #moving
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_speed > 0: #left
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + player.get_width() < WIDTH: #right
            player.x += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0: #up
            player.y -= player_speed
        if keys[pygame.K_s] and player.y + player_speed + player.get_height() < HEIGHT: #down
            player.y += player_speed
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:

            enemy.move(enemy_speed)
            #check hiting the player
            enemy.move_projectiles(projectile_speed, player)
            #enemy shoot you
            if random.randrange(0, 120) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 30
                enemies.remove(enemy)
                kills += 1
            # check hiting the enemy
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        player.move_projectiles(-projectile_speed, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WINDOW.blit(BACKGROUND, (0,0))
        title_label = title_font.render("Press to Play", 1, (255,255,255))
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()