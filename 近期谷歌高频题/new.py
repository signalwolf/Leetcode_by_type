# My method:
from collections import defaultdict, deque
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        node_to_bus = defaultdict(set)
        bus_map = defaultdict(set)

        # build node to bus
        for i, route in enumerate(routes):
            for node in route:
                if node not in node_to_bus:
                    node_to_bus[node].add(i)
                else:
                    node_to_bus[node].add(i)
                    bus_map[i] = bus_map[i].union(node_to_bus[node])
                    for bus in node_to_bus[node]:
                        bus_map[bus].add(i)

        curr_bus_set = node_to_bus[S]
        end_bus_set = node_to_bus[T]
        # queue = deque([start_bus])
        visited = set()
        dis = 1
        # print node_to_bus, bus_map
        while curr_bus_set:
            if len(curr_bus_set) > len(end_bus_set):
                curr_bus_set, end_bus_set = end_bus_set, curr_bus_set
            next_bus_set = set()
            for curr_bus in curr_bus_set:
                visited.add(curr_bus)
                if curr_bus in end_bus_set:
                    return dis
                for ngb in bus_map[curr_bus]:
                    if ngb not in visited:
                        next_bus_set.add(ngb)
            curr_bus_set = next_bus_set

            dis += 1
        return -1


from collections import deque
class Solution:
    # This is a very good BFS problem.
    # In BFS, we need to traverse all positions in each level firstly, and then go to the next level.
    # Our task is to figure out:
    # 1. What is the level in this problem?
    # 2. What is the position we want in this problem?
    # 3. How to traverse all positions in a level?
    #
    # For this problem:
    # 1. The level is each time to take bus.
    # 2. The position is all of the stops you can reach for taking one time of bus.
    # 3. Using a queue to record all of the stops can be arrived for each time you take buses.
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # You already at the terminal, so you needn't take any bus.
        if S == T: return 0

        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)

        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([S])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()

        res = 0
        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stopBoard[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T: return res
                        queue.append(stop)
        return -1