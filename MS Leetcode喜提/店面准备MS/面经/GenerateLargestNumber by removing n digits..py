
# coding=utf-8

# 千万不要忘记stack的size可能超过最后的需要的size，于是要删除掉相关的东西
def largestNum(num, k):
    # special case handle:
    # 1. len(num) <= k: return 0
    # 2. heading zeros.
    # 3. num is positive

    # special handle
    if int(num) <= 0: return 0
    if len(num) <= k: return 0

    # greedy:
    # always select the largest number between num[0:k]
    stack = []
    realK = len(num) - k
    for i in xrange(len(num)):
        while k and stack and stack[-1] < num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])
        if k == 0:
            break
    return ''.join(stack[:realK]) + num[i + 1:]

print largestNum('54321', 1)
