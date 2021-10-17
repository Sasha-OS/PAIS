import GlobalVariables as GV


class Projectile:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = GV.PG_LIB.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


    def move(self, speed):
        self.y += speed

    def off_screen(self, height):
        return not(self.y < height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


def collide(obj1, obj2):        # чи дотикнулись об'єкти
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, int(offset_y))) is not None
