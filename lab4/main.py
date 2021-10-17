import GlobalVariables as GV
import Algorytms
import time
import numpy
import math


def main():
    run = True
    clock = GV.PG_LIB.time.Clock()
    GV.PG_LIB.display.set_caption("Space Invaders")

    def redraw_window():
        GV.WINDOW.blit(GV.BACKGROUND, (0,0))
        #display info
        lives_label = GV.main_font.render(f"Lives: {GV.lives}", 1, (255, 5, 5))
        level_label = GV.main_font.render(f"Level: {GV.level}", 1, (255, 5, 5))
        kills_label = GV.main_font.render(f"Count: {GV.kills}", 1, (255, 5, 5))

        GV.WINDOW.blit(level_label, (10, 10))
        GV.WINDOW.blit(kills_label, (10, 50))
        GV.WINDOW.blit(lives_label, (GV.WIDTH - level_label.get_width() - 10, 10))
        for enemy in GV.enemies:
            enemy.draw(GV.WINDOW)
        for asteroid in GV.asteroids:
            asteroid.draw()
        for pixel in GV.pixelPath:
            pixel.draw()

        if GV.lost:
            lost_label = GV.lost_font.render("You lost...", 1, (255, 10, 10))
            GV.WINDOW.blit(lost_label, (GV.WIDTH/2 - lost_label.get_width()/2, 350))

        GV.player.draw(GV.WINDOW)


        GV.PG_LIB.display.update()

    while run:
        clock.tick(GV.FPS)
        redraw_window()
        if GV.lives <= 0 or GV.player.health <= 0:
            GV.lost = True
            GV.lost_count += 1

        if GV.lost:
            run = False
            #need to fix bug
            # if GV.lost_count > GV.FPS * 3:
            #     with open('report.txt', 'a') as the_file:
            #         the_file.write(
            #             f'level: {GV.level} lost, time: {time.time() - GV.time} seconds, kills: {GV.kills} \n')
            # else:
            #     continue

        if len(GV.enemies) == 0:

            GV.level += 1
            GV.wave_length += 5
            #spawn enemies
            for i in range(GV.wave_length):
                enemy = GV.SC.Enemy(GV.random.randrange(100, GV.WIDTH-150), GV.random.randrange(-1500, -100), GV.random.choice(["red", "blue", "green"]))
                GV.enemies.append(enemy)
            for i in range(GV.wave_length):
                asteroid = GV.AsteroidClass.Asteroid(GV.random.randrange(100, GV.WIDTH-100), GV.random.randrange(-1500, -100))
                GV.asteroids.append(asteroid)
        for event in GV.PG_LIB.event.get():
            if event.type == GV.PG_LIB.QUIT:
                run = False
        #moving
        keys = GV.PG_LIB.key.get_pressed()
        if keys[GV.PG_LIB.K_a] and GV.player.x - GV.player_speed > 0: #left
            GV.player.x -= GV.player_speed
        if keys[GV.PG_LIB.K_d] and GV.player.x + GV.player_speed + GV.player.get_width() < GV.WIDTH: #right
            GV.player.x += GV.player_speed
        if keys[GV.PG_LIB.K_w] and GV.player.y - GV.player_speed > 0: #up
            GV.player.y -= GV.player_speed
        if keys[GV.PG_LIB.K_s] and GV.player.y + GV.player_speed + GV.player.get_height() < GV.HEIGHT: #down
            GV.player.y += GV.player_speed

        GV.player.shoot()
        GV.time = time.time()
        for enemy in GV.enemies[:]:

            enemy.move(GV.enemy_speed)
            #check hiting the player
            enemy.move_projectiles(GV.projectile_speed, GV.player)
            #enemy shoot you
            if GV.RANDOM_LIB.randrange(0, 120) == 1:
                enemy.shoot()
            if GV.ProjectileClass.collide(enemy, GV.player):
                GV.player.health -= 30
                GV.enemies.remove(enemy)
                GV.kills += 1
            # check hiting the enemy
            if enemy.y + enemy.get_height() > GV.HEIGHT:
                GV.lives -= 1
                GV.enemies.remove(enemy)
        GV.player.move_projectiles(-GV.projectile_speed, GV.enemies)
        GV.player.move_projectiles(-GV.projectile_speed, GV.asteroids)
        for asteroid in GV.asteroids[:]:
            asteroid.move(GV.enemy_speed + 1)

            if GV.ProjectileClass.collide(asteroid, GV.player):
                GV.player.health -= 10
                GV.asteroids.remove(asteroid)

        Algorytms.enemyArray = []
        Algorytms.arrayOfPath = []
        GV.pixelPath = []
        Algorytms.createVisitMatrix(Algorytms.matrix)
        Algorytms.fillMatrix(Algorytms.matrix)
        # for i in Algorytms.matrix:
        #     print(*i)
        if Algorytms.enemyArray:
            Algorytms.emptyMatrix(Algorytms.visited, [int(GV.player.y / 50), int(GV.player.x / 50)])
            Algorytms.emptyMatrix(Algorytms.matrix, [int(GV.player.y / 50), int(GV.player.x / 50)])

            workingTree = Algorytms.Tree
            print(Algorytms.enemyArray)
            workingTree.createTree(workingTree)

            workingTree.current = workingTree.startNode

            Algorytms.fill0()
            workingTree.setRate(workingTree)

            workingTree.current = workingTree.startNode
            for i in Algorytms.matrix:
                print(*i)

        Algorytms.moveEnemy()
        Algorytms.enemyArray = []
        redraw_window()


def main_menu():
    title_font = GV.PG_LIB.font.SysFont("comicsans", 70)
    run = True
    while run:
        GV.WINDOW.blit(GV.BACKGROUND, (0,0))
        title_label = title_font.render("Press to Play", 1, (255,255,255))
        GV.WINDOW.blit(title_label, (GV.WIDTH/2 - title_label.get_width()/2, 350))
        GV.PG_LIB.display.update()
        for event in GV.PG_LIB.event.get():
            if event.type == GV.PG_LIB.QUIT:
                run = False
            if event.type == GV.PG_LIB.MOUSEBUTTONDOWN:
                main()
    GV.PG_LIB.quit()


main_menu()