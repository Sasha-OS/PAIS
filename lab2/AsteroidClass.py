import GlobalVariables as GV


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 1
        self.asteroid_img = GV.ASTEROID_PICTURE
        self.mask = GV.PG_LIB.mask.from_surface(self.asteroid_img)
    def draw(self):
        GV.WINDOW.blit(self.asteroid_img, (self.x, self.y))

    def move(self, speed):
        self.y += speed
