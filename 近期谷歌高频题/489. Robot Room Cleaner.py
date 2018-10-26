# coding=utf-8
# 千万注意的是robot的移动中还一定要包含direction，不能对上来的direction做任何的假设

class Solution(object):
    def dfs(self, robot, visited, position, direction):
        robot.clean()
        visited.add(position)
        direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        index = direction_list.index(direction)
        for i in xrange(4):
            nx, ny = position[0] + direction[0], position[1] + direction[1]
            if (nx, ny) not in visited and robot.move():
                self.dfs(robot, visited, (nx, ny), direction)
            robot.turnLeft()
            index = (index + 1) % 4
            direction = direction_list[index]

        if position == (0, 0):
            return
        else:
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            return

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        self.dfs(robot, visited, (0, 0), (-1, 0))