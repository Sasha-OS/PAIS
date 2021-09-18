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
            if GV.lost_count > GV.FPS * 3:
                run = False
            else:
                continue

        if len(GV.enemies) == 0:
            GV.level += 1
            GV.wave_length += 5
            #spawn enemies
            for i in range(GV.wave_length):
                enemy = GV.SC.Enemy(GV.random.randrange(100, GV.WIDTH-100), GV.random.randrange(-1500, -100), GV.random.choice(["red", "blue", "green"]))
                GV.enemies.append(enemy)
            for i in range(GV.wave_length + 10):
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
        if keys[GV.PG_LIB.K_SPACE]:
            GV.player.shoot()
        if keys[GV.PG_LIB.K_z]:
             GV.work = True
             if GV.currAlg == "dfs":
                print("current alg bfs")
                GV.currAlg = "bfs"
             elif GV.currAlg == "bfs":
                print("current alg ucs")
                GV.currAlg = "ucs"
             elif GV.currAlg == "ucs":
                print("current alg dfs")
                GV.currAlg = "dfs"
             Algorytms.arrOfPath = []
             Algorytms.arrOfList = []
             Algorytms.listOfVisited = []
             Algorytms.matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
             Algorytms.visitMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
             Algorytms.path = [[math.ceil(int(GV.player.x / 50)), math.ceil(int(GV.player.y / 50))]]
             Algorytms.numofEnemy = 1  # TODO: get num from matrix
             Algorytms.arrOfPath = []
             Algorytms.listOfVisited = [[math.ceil(int(GV.player.x / 50)), math.ceil(int(GV.player.y / 50))]]
             Algorytms.arrOfList = []
             Algorytms.arrBeforePath = []
             Algorytms.ucsListOfVisited = [[math.ceil(int(GV.player.x / 50)), math.ceil(int(GV.player.y / 50))]]
             Algorytms.lenMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
             Algorytms.ucsList = []
             Algorytms.arrUcsList = []
             Algorytms.enemyCoords = []
             if len(Algorytms.path) > 1:
                GV.pixelPath = []
             if len(Algorytms.listOfVisited) > 1:
                GV.pixelPath = []


        if keys[GV.PG_LIB.K_x]:
            if GV.work == True:
                Algorytms.createStartMatrix()
                print(Algorytms.matrix)
                if GV.currAlg == "dfs":
                    GV.work = False
                    start_time = time.time()

                    while Algorytms.numofEnemy > 0:
                        if len(Algorytms.path) > 1:
                            Algorytms.matrix[Algorytms.path[-1][0]][Algorytms.path[-1][1]] = 3
                            Algorytms.arrOfPath.append(Algorytms.path)
                            Algorytms.path = [Algorytms.arrOfPath[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.dfs(Algorytms.matrix, Algorytms.visitMatrix)
                    for i in Algorytms.arrOfPath:
                        print(*i)
                    print("--- %s seconds ---" % (time.time() - start_time))

                    if len(Algorytms.path) > 0:
                        GV.pixelPath = []
                        for i in Algorytms.path:
                            pix = GV.AsteroidClass.Pixel(int(i[1] * 50), int(i[0] * 50))
                            GV.pixelPath.append(pix)


                if GV.currAlg == "bfs":
                    start_time = time.time()
                    GV.work = False
                    while Algorytms.numofEnemy > 0:
                        # print(path)
                        if len(Algorytms.listOfVisited) > 1:
                            Algorytms.matrix[Algorytms.listOfVisited[-1][0]][Algorytms.listOfVisited[-1][1]] = 3
                            # print(arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.listOfVisited)
                            #listOfVisited = [Algorytms.arrOfList[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.bfs(Algorytms.matrix, Algorytms.visitMatrix)

                    for i in Algorytms.arrOfList:
                        print(*i)
                    print("--- %s seconds ---" % (time.time() - start_time))

                    if len(Algorytms.listOfVisited) > 0:
                        GV.pixelPath = []
                        for i in Algorytms.listOfVisited:
                            pix = GV.AsteroidClass.Pixel(int(i[0] * 50), int(i[1] * 50))
                            GV.pixelPath.append(pix)

                if GV.currAlg == "ucs":
                    start_time = time.time()
                    GV.work = False
                    while Algorytms.numofEnemy > 0:
                        # print(path)
                        if len(Algorytms.ucsListOfVisited) > 1:
                            Algorytms.matrix[Algorytms.ucsListOfVisited[-1][0]][Algorytms.ucsListOfVisited[-1][1]] = 3
                            # print(arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.ucsListOfVisited)
                            Algorytms.ucsListOfVisited = [Algorytms.arrOfList[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.ucs(Algorytms.matrix, Algorytms.visitMatrix)
                    Algorytms.findEnemyCoords(Algorytms.matrix)

                    for i in Algorytms.lenMatrix:
                        print(*i)
                    print("Enemy array:")
                    print(Algorytms.enemyCoords)
                    for i in Algorytms.enemyCoords:
                        curr = i
                        minimum = 10000
                        next = []
                        while minimum != 1:
                            if curr:
                                Algorytms.ucsList.append(curr)
                            if curr and curr[0] - 1 >= 0 and 0 < Algorytms.lenMatrix[curr[0] - 1][curr[1]] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0] - 1][curr[1]]
                                next = [curr[0] - 1, curr[1]]
                            if curr and curr[1] - 1 >= 0 and 0 < Algorytms.lenMatrix[curr[0]][curr[1] - 1] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0]][curr[1] - 1]
                                next = [curr[0], curr[1] - 1]
                            if curr and curr[0] + 1 < 15 and 0 < Algorytms.lenMatrix[curr[0] + 1][curr[1]] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0] + 1][curr[1]]
                                next = [curr[0] + 1, curr[1]]
                            if curr and curr[1] + 1 < 15 and 0 < Algorytms.lenMatrix[curr[0]][curr[1] + 1] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0]][curr[1] + 1]
                                next = [curr[0], curr[1] + 1]
                            curr = next

                        Algorytms.arrUcsList.append(Algorytms.ucsList)
                        Algorytms.ucsList = []
                        print("--- %s seconds ---" % (time.time() - start_time))
                    # print(arrUcsList)
                    print("Distance matrix")

                    print("path to enemies:")
                    for i in Algorytms.arrUcsList:
                        print(*i)




                    if len(Algorytms.arrUcsList) > 0:
                        GV.pixelPath = []
                        for i in Algorytms.arrUcsList:
                            pix = GV.AsteroidClass.Pixel(int(i[1] * 50), int(i[0] * 50))
                            GV.pixelPath.append(pix)

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