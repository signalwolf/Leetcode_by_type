from random import randint
from collections import deque
def findNum(matrix, target):
    target = set(target)
    queue = deque()
    # format: distance, x, y
    queue.append([0,(0,0)])
    visited = set()
    while queue:
        dis, point = queue.popleft()
        currX, currY = point
        if matrix[currX][currY] in target:
            return dis
        visited.add(tuple([currX, currY]))
        for dx, dy in [[1,0], [0,1]]:
            nx, ny = currX + dx, currY + dy
            if tuple([nx, ny]) not in visited:
                queue.append([dis + 1, tuple([nx, ny])])
    return None


target = [1, 0, 9]
lenX, lenY = 10, 10
matrix = [[0 for _ in xrange(lenX)] for _ in xrange(lenY)]
for i in xrange(lenX):
    for j in xrange(lenY):
        matrix[i][j] = randint(0, 20)
    print matrix[i]

print findNum(matrix, target)