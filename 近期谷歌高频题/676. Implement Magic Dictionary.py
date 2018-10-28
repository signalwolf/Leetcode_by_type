# coding=utf-8


# 没考虑的情况是如果两个word本身就存在互相间的关系，那么你就不能exclude掉它
# 例如：
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# 第一个hello是true，因为hello match到了 hallo上。

# 但是有更简单的，见最后

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exclude = set()
        self.wordset = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.exclude.add(word)
            for i in xrange(len(word)):
                new_word = word[:i] + '_' + word[i + 1:]
                if new_word not in self.wordset:
                    self.wordset[new_word] = word
                elif self.wordset[new_word] == 0:
                    self.exclude.discard(word)
                else:
                    self.exclude.discard(self.wordset[new_word])
                    self.exclude.discard(word)
                    self.wordset[new_word] = 0

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if word in self.exclude: return False
        for i in xrange(len(word)):
            new_word = word[:i] + '_' + word[i + 1:]
            if new_word in self.wordset:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = {}
        self.dic = set([])

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.pool = {}
        for word in dict:
            self.dic.add(word)
            for i in range(len(word)):
                tmp = word[:i]+"*"+word[i+1:]
                if tmp in self.pool:
                    self.pool[tmp] += 1
                else:
                    self.pool[tmp] = 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            tmp = word[:i]+"*"+word[i+1:]
            if tmp in self.pool and (self.pool[tmp] > 1 or (self.pool[tmp] == 1 and word not in self.dic)):
                return True
        return False
