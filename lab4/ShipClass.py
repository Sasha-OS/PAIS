import GlobalVariables as GV

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
            if projectile.off_screen(GV.HEIGHT):
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
            projectile = GV.ProjectileClass.Projectile(self.x, self.y, self.projectile_img)
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
        self.ship_img = GV.SHIP_YELLOW
        self.projectile_img = GV.YELLOW_PROJECTILE
        self.mask = GV.PG_LIB.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_projectiles(self, speed, objs):
        self.cooldown()
        for projectile in self.projectiles:
            projectile.move(speed)
            if projectile.off_screen(GV.HEIGHT):
                self.projectiles.remove(projectile)
            else: #kill enemy
                for obj in objs:
                    if projectile.collision(obj):
                        obj.health -= 10
                        if obj.health <= 0:
                            objs.remove(obj)
                            GV.kills += 1
                        if projectile in self.projectiles:
                            self.projectiles.remove(projectile)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        GV.PG_LIB.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        GV.PG_LIB.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))




class Enemy(Ship):
    def __init__(self, x, y, color, health=15):
        super().__init__(x, y, health)
        self.ship_img, self.projectile_img = GV.COLOR_MAP[color]
        self.mask = GV.PG_LIB.mask.from_surface(self.ship_img)
        self.max_health = health

    def move(self, speed):
        self.y += speed

    def shoot(self):
        if self.cool_down_counter == 0:
            projectile = GV.ProjectileClass.Projectile(self.x-20, self.y, self.projectile_img)
            self.projectiles.append(projectile)
            self.cool_down_counter = 1

    def enemyhealthbar(self, window):
        GV.PG_LIB.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        GV.PG_LIB.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))

    def draw(self, window):
        super().draw(window)
        self.enemyhealthbar(window)