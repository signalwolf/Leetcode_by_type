from collections import defaultdict, deque


class Solution(object):
    def BFS(self, graph, query):
        a, b = query
        if a not in graph or b not in graph: return -1.0
        queue = deque([[a, 1, 1]])
        visited = set([a])
        while queue:
            curr, up, down = queue.popleft()
            if curr == b:
                return up / float(down) if down != 0.0 else -1.0
            for neighbor in graph[curr]:
                ngb, new_up, new_down = neighbor
                if ngb not in visited:
                    visited.add(ngb)
                    queue.append([ngb, new_up * up, new_down * down])
        return -1.0

    def buildGraph(self, equations, values):
        graph = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].append([b, values[i], 1])
            graph[b].append([a, 1, values[i]])
        return graph

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = self.buildGraph(equations, values)
        # print graph
        res = []
        for query in queries:
            res.append(self.BFS(graph, query))
        return res
