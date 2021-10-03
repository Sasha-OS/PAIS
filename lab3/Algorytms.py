import GlobalVariables as gv
import numpy

# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
lenMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
pointToResp = [600, 350]
path = []
numofEnemy = 9
startPoint = [13, 7]
curr = [13, 7]
enemyArray = []
arrayOfPath = []

def findAsteroids(matr):
    for i in range(0, len(matr)):
        for j in range(0, len(matr[i])):
            if matr[i][j] == 3:
                lenMatrix[i][j] = 999


def fillMatrix(matrix):
    for i in gv.enemies:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 2
    for i in gv.asteroids:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 3

def createVisitMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                enemyArray.append([i, j])

def emptyMatrix(matr, cur):
    global curr
    for i in range(0, len(matr) - 1):
        for j in range(0, len(matr[i]) - 1):
            if not matr[i][j] == 0:
                matr[i][j] = 0
    matr[cur[0]][cur[1]] = 1
    # for i in matr:
    #     print(*i)
#TODO: add baricades(3)

#distance between points
def distanceBetweenPoints(cur, startPoiint):
    distance = 0
    if cur[0] > startPoiint[0]:
        distance += cur[0] - startPoiint[0]
    else:
        distance += startPoiint[0] - cur[0]
    if cur[1] > startPoiint[1]:
        distance += cur[1] - startPoiint[1]
    else:
        distance += startPoiint[1] - cur[1]
    return distance


def lenFinal(curr):
    return distanceBetweenPoints(curr, startPoint) + distanceBetweenPoints(curr, enemyArray[0]) * 2




def gotEnemy(cur):
    if 0 <= cur[0] + 1 < 15 and 0 <= cur[1] + 1 < 15 and lenMatrix[cur[0] + 1][cur[1] + 1] == -1:
        return True
    elif 0 <= cur[0] - 1 < 15 and 0 <= cur[1] - 1 < 15 and lenMatrix[cur[0] - 1][cur[1] - 1] == -1:
        return True
    elif 0 <= cur[0] + 1 < 15 and 0 <= cur[1] - 1 < 15 and lenMatrix[cur[0] + 1][cur[1] - 1] == -1:
        return True
    elif 0 <= cur[0] - 1 < 15 and 0 <= cur[1] + 1 < 15 and lenMatrix[cur[0] - 1][cur[1] + 1] == -1:
        return True
    elif 0 <= cur[0] < 15 and 0 <= cur[1] + 1 < 15 and lenMatrix[cur[0]][cur[1] + 1] == -1:
        return True
    elif 0 <= cur[0] + 1 < 15 and 0 <= cur[1] < 15 and lenMatrix[cur[0] + 1][cur[1]] == -1:
        return True
    elif 0 <= cur[0] < 15 and 0 <= cur[1] - 1 < 15 and lenMatrix[cur[0]][cur[1] - 1] == -1:
        return True
    elif 0 <= cur[0] - 1 < 15 and 0 <= cur[1] < 15 and lenMatrix[cur[0] - 1][cur[1]] == -1:
        return True
    else:
        return False


def setWay(cur):
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1] + 1] == 300:
        lenMatrix[cur[0] + 1][cur[1] + 1] = lenFinal([cur[0] + 1, cur[1] + 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1] - 1] == 300:
        lenMatrix[cur[0] - 1][cur[1] - 1] = lenFinal([cur[0] - 1, cur[1] - 1])
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1] - 1] == 300:
        lenMatrix[cur[0] + 1][cur[1] - 1] = lenFinal([cur[0] + 1, cur[1] - 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1] + 1] == 300:
        lenMatrix[cur[0] - 1][cur[1] + 1] = lenFinal([cur[0] - 1, cur[1] + 1])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0]][cur[1] + 1] == 300:
        lenMatrix[cur[0]][cur[1] + 1] = lenFinal([cur[0], cur[1] + 1])
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1]] == 300:
        lenMatrix[cur[0] + 1][cur[1]] = lenFinal([cur[0] + 1, cur[1]])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0]][cur[1] - 1] == 300:
        lenMatrix[cur[0]][cur[1] - 1] = lenFinal([cur[0], cur[1] - 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1]] == 300:
        lenMatrix[cur[0] - 1][cur[1]] = lenFinal([cur[0] - 1, cur[1]])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0]][cur[1]] == 300:
        lenMatrix[cur[0]][cur[1]] = lenFinal([cur[0], cur[1]])

def dodge():
    global arrayOfPath
    for i in gv.enemies:
        if i.x == gv.player.x and 700 > i.x > 50:
            if [int(i.y / 50), int(i.x / 50)] in enemyArray:
                enemyArray.remove([int(i.y / 50), int(i.x / 50)])
            if [int(i.x / 50), int(i.y / 50)] in enemyArray:
                enemyArray.remove([int(i.x / 50), int(i.y / 50)])
            buf = gv.RANDOM_LIB.choice([1, 0])
            if buf == 0:
                i.x += 50
            else:
                i.x -= 50

    arrayOfPath = []
    createVisitMatrix(matrix)
    fillMatrix(matrix)

def chooseSmall(matrix):
    value = 1000
    currentVay = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if not matrix[i][j] == -1 and matrix[i][j] > 0:
                if matrix[i][j] < value:
                    value = matrix[i][j]
                    currentVay = [i, j]
    return currentVay


def main_alg(curr):
    lenMatrix[enemyArray[0][0]][enemyArray[0][1]] = -1
    if not gotEnemy(curr):
        setWay(curr)
        path.append(curr)
        curr = chooseSmall(lenMatrix)
        #print(curr)
        main_alg(curr)

def round50(n):
    return round(n * 2, -2) // 2
