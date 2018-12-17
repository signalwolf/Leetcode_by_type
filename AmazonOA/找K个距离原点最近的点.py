
from heapq import heappop, heappush

def disCalc(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2

def findKclosePoint(original, points, k):
    # max heap with size K to solve the problem.
    # if the heap size large than K, then pop out from max heap
    # otherwise, heappush to the node

    # special case: k , points
    # k == 0: ? return []
    # k == len(points), return points
    # k > len(points): return points
    # len(points) == 0: return []

    if k == 0 or len(points) == 0:
        return []
    if k >= len(points):
        return points

    heap = []
    for point in points:
        currDistance = disCalc (original, point)
        heappush(heap, [-currDistance, point])
        if len(heap) > k:
            heappop(heap)

    return [tmp[1] for tmp in heap]

print findKclosePoint([0, 0], [[1,1], [2,2], [1,3], [2,4],[0,1],[1, 0]], 5)
