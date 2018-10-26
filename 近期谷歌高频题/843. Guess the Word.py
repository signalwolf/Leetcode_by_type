# coding=utf-8
# 最简单的方法：每次都缩减list，而缩减的方法就是每次计算我去guess的word与其他word之间match的值
# 当match的值与guess的结果一致的时候就代表它可以在下次的列表中。这样是最快的方法，但是却不是使用
# 最少的次数来猜出secret word的方法

from random import randint
class Solution(object):
    def findSecretWord(self, wordlist, master):
        def dis_cal(w1, w2):
            count = 0
            for i in xrange(6):
                if w1[i] == w2[i]:
                    count += 1
            return count

        N = len(wordlist)
        curr_list = wordlist
        for _ in xrange(10):
            curr_index = randint(0, len(curr_list) - 1)
            curr_word = curr_list[curr_index]
            next_list = []
            match = master.guess(curr_word)
            if match == 6: return
            for i in xrange(len(curr_list)):
                if i == curr_index: continue
                if dis_cal(curr_list[i], curr_word) == match:
                    next_list.append(curr_list[i])
            curr_list = next_list

# 为了使用更少的此时来猜出secret word，那么就要在缩小word的过程中进行优化。
# 考虑到如果一个word与很多其他的word都没有相交的情况：
# 如果secret word 与其完全不相交，那么这次filter掉的就很少
# 如果secret word 与其相交，那么filter掉了很多
# 我个人觉得如果