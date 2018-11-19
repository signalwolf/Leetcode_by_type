class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 1.0.0 == 1
        # 1.01  == 1.1
        if not version1 and not version2: return 0
        if not version1: return 1
        if not version2: return -1
        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        for i in xrange(min(len(version1), len(version2))):
            if version1[i] == version2[i]:
                continue
            elif version1[i] > version2[i]:
                return 1
            else:
                return -1
        else:
            if len(version1) == len(version2) == i + 1:
                return 0
            elif len(version1) == i + 1:
                for j in xrange(i + 1, len(version2)):
                    if version2[j] != 0:
                        return -1
                else:
                    return 0
            else:
                for j in xrange(i + 1, len(version1)):
                    if version1[j] != 0:
                        return 1
                else:
                    return 0