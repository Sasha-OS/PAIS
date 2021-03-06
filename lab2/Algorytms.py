import GlobalVariables as gv
import numpy
import math

# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
visitMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
path = [[math.ceil(int(gv.player.x/50)), math.ceil(int(gv.player.y/50))]]
numofEnemy = 1 # TODO: get num from matrix
arrOfPath = []
listOfVisited = [[math.ceil(int(gv.player.x/50)), math.ceil(int(gv.player.y/50))]]
arrOfList = []
arrBeforePath = []
ucsListOfVisited = [[math.ceil(int(gv.player.x/50)), math.ceil(int(gv.player.y/50))]]
lenMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
ucsList = []
arrUcsList = []
enemyCoords = []


def createStartMatrix():
    for i in gv.asteroids:
                if 0 < int(i.x/50 )< len(matrix) and 0 < int(i.y/50) < len(matrix):
                    matrix[math.ceil(int(i.y/50))][math.ceil(int(i.x/50))] = 3
                    gv.VisitMatrix[math.ceil(int(i.y/50))][math.ceil(int(i.x/50))] = 1
    for i in gv.enemies:
                if 0 < int(i.x/50) < len(matrix) and 0 < int(i.y/50) < len(matrix):
                    matrix[math.ceil(int(i.y/50))][math.ceil(int(i.x/50))] = 2
                    gv.VisitMatrix[math.ceil(int(i.y/50))][math.ceil(int(i.x/50))] = 1

    # global numofEnemy, path
    # for i in matrix:
    #     for j in i:
    #         if j == 2:
    #             numofEnemy += 1
    #         if j == 1:
    #             path = [[int(gv.GOOD_SHIP.x / 50), int(gv.GOOD_SHIP.y / 50)]]

    matrix[0][0] = 0
    matrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1
    gv.VisitMatrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1




def createVisitMatrix(matrix, visitMatrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                visitMatrix[i][j] = 1
            else:
                visitMatrix[i][j] = 0


def dfs(matrix, visitMatrix, curX=path[-1][0], curY=path[-1][1]):
    # print(path)
    # for i in visitMatrix:
    #     print(*i)
    visitMatrix[curX][curY] = 1
    while len(path) > 0:
        curX = path[-1][0]
        curY = path[-1][1]
        if curX + 1 < len(matrix) and matrix[curX + 1][curY] == 2:
            path.append([curX + 1, curY])
            break
        elif curY + 1 < len(matrix) and matrix[curX][curY + 1] == 2:
            path.append([curX, curY + 1])
            break
        elif curX - 1 >= 0 and matrix[curX - 1][curY] == 2:
            path.append([curX - 1, curY])
            break
        elif curY - 1 >= 0 and matrix[curX][curY - 1] == 2:
            path.append([curX, curY - 1])
            break

        step = False
        # print(path)
        # for i in visitMatrix:
        #     print(*i)
        if curX + 1 < len(matrix) and visitMatrix[curX + 1][curY] == 0 and not step:
            visitMatrix[curX + 1][curY] = 1
            path.append([curX + 1, curY])
            step = True
        elif curY + 1 < len(matrix) and visitMatrix[curX][curY + 1] == 0 and not step:
            visitMatrix[curX][curY + 1] = 1
            path.append([curX, curY + 1])
            step = True
        elif curY - 1 >= 0 and visitMatrix[curX][curY - 1] == 0 and not step:
            visitMatrix[curX][curY - 1] = 1
            path.append([curX, curY - 1])
            step = True
        elif curX - 1 >= 0 and visitMatrix[curX - 1][curY] == 0 and not step:
            visitMatrix[curX - 1][curY] = 1
            path.append([curX - 1, curY])
            step = True
        elif not step:
            path.remove(path[-1])


def bfs(matrix, visitMatrix, curX=listOfVisited[-1][0], curY=listOfVisited[-1][1]):
    listOfVisited.append([curX, curY])
    while len(listOfVisited) > 0:
        #print(listOfVisited)
        # for i in visitMatrix:
        #     print(*i)
        curX = listOfVisited[0][0]
        curY = listOfVisited[0][1]
        if curX + 1 < len(matrix) and matrix[curX + 1][curY] == 2:
            listOfVisited.append([curX + 1, curY])
            break
        elif curY + 1 < len(matrix) and matrix[curX][curY + 1] == 2:
            listOfVisited.append([curX, curY + 1])
            break
        elif curX - 1 >= 0 and matrix[curX - 1][curY] == 2:
            listOfVisited.append([curX - 1, curY])
            break
        elif curY - 1 >= 0 and matrix[curX][curY - 1] == 2:
            listOfVisited.append([curX, curY - 1])
            break
        step = False
        # print(path)
        # for i in visitMatrix:
        #     print(*i)
        if curX + 1 < len(matrix) and visitMatrix[curX + 1][curY] == 0:
            visitMatrix[curX + 1][curY] = 1
            listOfVisited.append([curX + 1, curY])

        if curY + 1 < len(matrix) and visitMatrix[curX][curY + 1] == 0:
            visitMatrix[curX][curY + 1] = 1
            listOfVisited.append([curX, curY + 1])

        if curY - 1 >= 0 and visitMatrix[curX][curY - 1] == 0:
            visitMatrix[curX][curY - 1] = 1
            listOfVisited.append([curX, curY - 1])

        if curX - 1 >= 0 and visitMatrix[curX - 1][curY] == 0:
            visitMatrix[curX - 1][curY] = 1
            listOfVisited.append([curX - 1, curY])
        arrBeforePath.append(path[-1])
        listOfVisited.remove(listOfVisited[0])



def ucs(matrix, visitMatrix, curX=ucsListOfVisited[-1][0], curY=ucsListOfVisited[-1][1]):
    ucsListOfVisited.append([curX, curY])
    while len(ucsListOfVisited) > 0:
        # print(ucsListOfVisited)
        # for i in visitMatrix:
        #     print(*i)
        curX = ucsListOfVisited[0][0]
        curY = ucsListOfVisited[0][1]
        if curX + 1 < len(matrix) and matrix[curX + 1][curY] == 2:
            ucsListOfVisited.append([curX + 1, curY])
            break
        elif curY + 1 < len(matrix) and matrix[curX][curY + 1] == 2:
            ucsListOfVisited.append([curX, curY + 1])
            break
        elif curX - 1 >= 0 and matrix[curX - 1][curY] == 2:
            ucsListOfVisited.append([curX - 1, curY])
            break
        elif curY - 1 >= 0 and matrix[curX][curY - 1] == 2:
            ucsListOfVisited.append([curX, curY - 1])
            break
        step = False
        # print(path)
        # for i in visitMatrix:
        #     print(*i)
        if curX + 1 < len(matrix) and visitMatrix[curX + 1][curY] == 0:
            if lenMatrix[curX + 1][curY] == 0:
                lenMatrix[curX + 1][curY] = lenMatrix[curX][curY] + 1
            elif lenMatrix[curX + 1][curY] > lenMatrix[curX][curY] + 1:
                lenMatrix[curX + 1][curY] = lenMatrix[curX][curY] + 1
            visitMatrix[curX + 1][curY] = 1
            ucsListOfVisited.append([curX + 1, curY])

        if curY + 1 < len(matrix) and visitMatrix[curX][curY + 1] == 0:
            if lenMatrix[curX][curY + 1] == 0:
                lenMatrix[curX][curY + 1] = lenMatrix[curX][curY] + 1
            elif lenMatrix[curX][curY + 1] > lenMatrix[curX][curY] + 1:
                lenMatrix[curX][curY + 1] = lenMatrix[curX][curY] + 1
            visitMatrix[curX][curY + 1] = 1
            ucsListOfVisited.append([curX, curY + 1])

        if curY - 1 >= 0 and visitMatrix[curX][curY - 1] == 0:
            if lenMatrix[curX][curY - 1] == 0:
                lenMatrix[curX][curY - 1] = lenMatrix[curX][curY] + 1
            elif lenMatrix[curX][curY - 1] > lenMatrix[curX][curY] + 1:
                lenMatrix[curX][curY - 1] = lenMatrix[curX][curY] + 1
            visitMatrix[curX][curY - 1] = 1
            ucsListOfVisited.append([curX, curY - 1])

        if curX - 1 >= 0 and visitMatrix[curX - 1][curY] == 0:
            if lenMatrix[curX - 1][curY] == 0:
                lenMatrix[curX - 1][curY] = lenMatrix[curX][curY] + 1
            elif lenMatrix[curX - 1][curY] > lenMatrix[curX][curY] + 1:
                lenMatrix[curX - 1][curY] = lenMatrix[curX][curY] + 1
            visitMatrix[curX - 1][curY] = 1
            ucsListOfVisited.append([curX - 1, curY])
        arrBeforePath.append(path[-1])
        ucsListOfVisited.remove(ucsListOfVisited[0])


def findEnemyCoords(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                enemyCoords.append([i, j])