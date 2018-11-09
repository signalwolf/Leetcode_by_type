class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def update(s, index):
            if index == len(s): return ['']

            if visited[index] is not False:
                return visited[index]
            res = []
            for i in xrange(index + 1, len(s) + 1):
                if s[index: i] in wordDict:
                    base = s[index: i]
                    answers = update(s, i)
                    for ans in answers:
                        if ans != '':
                            res.append(base + ' ' + ans)
                        else:
                            res.append(base)
            visited[index] = res
            return res

        if len(s) == 0: return ['']
        visited = [False] * len(s)
        wordDict = set(wordDict)
        update(s, 0)
        return visited[0]