# coding=utf-8

# 第一轮
# 一个十进制的正数转26进制的数a-z，1对应A，不是0index的，所以corner case比较多
#
# 第二轮，
# 给一个coin amount array，做coin change，先讨论了什么时候能用greedy 什么时候不能，然后写了greedy，bfs 和 dp解法
# 最后口述了A*，给了个收敛的heuristic函数
#
# 第三轮，用constant space traverse一个有parent指针和sibling指针的tree，不能recursion，不能建stack，不能修改树，我大四见过这个题，本科同学面头条被问到的，我们当时也没想出来。今天灵感来了就解了。
#
# 第四轮，设计Office word/excel 在resize时候的上边栏的按钮的显示与堆叠的切换，挖开之后实质是两种情况简单算法题，一个用greedy，另一个用binary search。
#
# 第五轮，LCA，H是树高度，给了O(H)解法，最后口述了O(log H)解法

# question 1:
def numconverter (num):
    base = ord('a')
    res = ''

    while num > 0:
        remain = num % 26 if num % 26 else 26
        res = chr(remain + base - 1) + res
        num = (num - remain) / 26
    return res

print numconverter(26)

# question2:

# question3:
# level order
