# coding=utf-8
# 思路:
# 1. clone graph 必然需要遍历整个graph, 此时可以使用BFS或者DFS
# 2. 如果使用BFS, 在queue中加入的值为：[curr_node, new_node]
# 3. new_neighbor = treenode(curr_node.neighbor), new_node.neighbor = new_neighbor


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return node
        new_node = UndirectedGraphNode(node.label)
        queue = deque([[node, new_node]])
        node_map = {}
        while queue:
            curr, clone = queue.popleft()
            node_map[curr] = clone
            for neighbor in curr.neighbors:
                if neighbor in node_map:
                    clone.neighbors.append(node_map[neighbor])
                else:
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    clone.neighbors.append(clone_neighbor)
                    queue.append([neighbor, clone_neighbor])
        return new_node