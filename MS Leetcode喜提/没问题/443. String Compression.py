class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, j, lens = 0, 0, len(chars)
        while i < lens:
            if i < lens - 1 and chars[i] == chars[i + 1]:
                count = 1
                while i < lens - 1 and chars[i] == chars[i + 1]:
                    count += 1
                    i += 1
                chars[j] = chars[i]
                j += 1
                for char in str(count):
                    chars[j] = char
                    j += 1
                i += 1
            else:
                chars[j] = chars[i]
                i += 1
                j += 1
        return j