# coding=utf-8

#一个matrix有的cell是P表示人，有的是B表示不能过。然后要求找每一个空的cell到最近的P的距离

# 最近的距离就应该想到BFS, 然后就是将距离为0的P点先加入到BFS queue中处理就好。

from collections import deque
def BFS(matrix):
    queue = deque([])
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if matrix[i][j] == 'p':
                queue.append([i, j, 0])
                matrix[i][j] = 0
            if matrix[i][j] == 'b':
                matrix[i][j] = -1

    M, N = len(matrix), len(matrix[0])

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in [[-1, 0], [0, -1], [1,0], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == '':
                matrix[nx][ny] = dist + 1
                queue.append([nx, ny, dist + 1])
    return matrix



matrix = [['' for _ in xrange(10)] for _ in xrange(10)]
matrix[1][5] = 'p'
matrix[3][8] = 'p'
matrix[8][5] = 'p'
matrix[5][5] = 'b'
ans = BFS(matrix)
for i in matrix:
    print i