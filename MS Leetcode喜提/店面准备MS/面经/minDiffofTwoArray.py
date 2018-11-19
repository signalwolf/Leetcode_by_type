from bisect import bisect_left, bisect_right
def minDiff(A, B):
    if not A or not B: return None

    # make sure A is always the smaller one:
    if len(A) > len(B):
        A, B = B, A

    res = float('inf')
    for i in xrange(len(A)):
        curr = A[i]
        index = bisect_left(B, curr)
        # A[index] >= curr
        # diff = A[index] - curr, curr - A[index - 1]
        if index == len(B):
            res = min(res, curr - B[-1])

        elif index == 0:
            res = min(res, B[0] - curr)

        else:
            res = min(B[index] - curr, curr - B[index - 1], res)
    return res

A = range(1, 100, 13)
B = range(-50, 10, 10)
print minDiff(A, B)