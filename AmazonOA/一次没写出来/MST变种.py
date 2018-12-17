
from collections import defaultdict
from heapq import heappush, heappop


def createEdge(graph):
    res = []
    for start in graph:
        for end in graph[start]:
            res.append([start, end, graph[start][end]])
    for edge in res:
        print edge
    return res

def helper(start, graph):
    # MST algorithm: Prim:
    # always get the smallest edge:

    parents = {}
    cost = {}
    visited = set()

    cost[start] = 0
    heap = [[0, start]]
    while heap:
        a, curr_node = heappop(heap)
        visited.add(curr_node)
        for ngb in graph[curr_node]:
            ngb_cost = graph[curr_node][ngb]
            if ngb in visited: continue
            if ngb not in cost or cost[ngb] > ngb_cost:
                cost[ngb] = ngb_cost
                parents[ngb] = curr_node
                heappush(heap, [ngb_cost, ngb])
        # print parents, heap


def MST(edges):
    v = set()
    graph = defaultdict(lambda: defaultdict(int))
    for start, end, cost in edges:
        v.add(start)
        v.add(end)
        graph[start][end] = cost

    cost, MSTedge = float('inf'), []
    for node in v:
        currCost, currMSTedge = helper(node, graph)
        if currCost < cost:
            MSTedge = currMSTedge

    return MSTedge

graph = {
    0:{1:4, 7:8},
    1:{0:4,7:11,2:8},
    2:{1:8, 8:2, 3:7, 5:4},
    3:{2:7,5:14,4:9},
    4:{3:9, 5:10},
    5:{3:14,6:2,4:10, 2:4},
    6:{7:1,8:6,5:2},
    7:{0:8,1:11,8:7,6:1},
    8:{2:2,6:6,7:7},
}



print MST(createEdge(graph))