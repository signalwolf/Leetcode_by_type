
from random import randint

from collections import deque
def shortestDistance(matrix):
    # BFS solution, 4 direction move
    queue = deque([])
    # format: distance, point
    queue.append([0, (0,0)])
    target = (len(matrix) - 1, len(matrix[0]) - 1)
    res = float('inf')
    visited = set()
    m, n = len(matrix), len(matrix[0])
    while queue:
        dis, currP = queue.popleft()
        if currP == target:
            return dis
        visited.add(currP)
        for dx, dy in \
                [[0, 1], [0, -1], [-1,0], [1, 0]]:
            nx, ny = currP[0] + dx, currP[1] + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] == 1:
                queue.append([dis + 1, (nx, ny)])
    return res

m, n = 5, 4
matrix = [[0 for i in xrange(n)] for _ in xrange(m)]
for i in xrange(m):
    for j in xrange(n):
        matrix[i][j] = randint(0, 1)
    print matrix[i]

matrix = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1]
]

print shortestDistance(matrix)