from heapq import heappush, heappop


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        grid, end = maze, destination
        distance = [[float('inf') for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        # print distance
        distance[start[0]][start[1]] = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        heap = [[0, start[0], start[1]]]
        while heap:
            dis, i, j = heappop(heap)
            # print i, j
            if [i, j] == end: return dis
            for direction in directions:
                dx, dy = direction
                nx, ny = i + dx, j + dy
                counter = 0
                while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
                    nx += dx
                    ny += dy
                    counter += 1
                # print direction, nx, ny, counter
                if counter == 0: continue
                nx -= dx
                ny -= dy
                if distance[nx][ny] > distance[i][j] + counter:
                    distance[nx][ny] = distance[i][j] + counter
                    heappush(heap, (distance[nx][ny], nx, ny))
        # print distance
        return -1