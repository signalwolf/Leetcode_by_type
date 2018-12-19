import time
def kDistinctLetter(s, k):
    # idea: sliding window solution
    # left, right = 0, 1 (right not included)
    # move right till num of distinct num == k
    # move left till num of distinct num == k - 1
    # start = left - 1, end = right (not included)
    # left = right, right = right + 1, list = [0] * 26


    if len(s) < k or k == 0:
        return None

    record = [0] * 26
    left, right, base = 0, 0, ord('a')
    lenS = len(s)
    res = None
    while left < lenS:
        # out condition: right = lenS or distineLetter == k
        while right < lenS and 26 - record.count(0) < k:
            record[ord(s[right]) - base] += 1
            right += 1

        if 26 - record.count(0) == k:
            # move left till distinct letter == k - 1
            while left < right and 26 - record.count(0) == k:
                record[ord(s[left]) - base] -= 1
                left += 1
            if not res:
                res = s[left - 1:right]
            else:
                if right - left + 1 < len(res):
                    res = s[left - 1: right]

        else:
            # out the loop
            left = right
    return res if res else -1

from collections import defaultdict
def substringKdis(input, k):
    if len(input) < k:
        return []
    letters = defaultdict(int)
    lo, hi = 0, 0
    ans = []
    while hi < len(input):
        if hi - lo + 1 <= k:
            letters[input[hi]] += 1
        else:
            letters[input[hi]] += 1
            letters[input[lo]] -= 1
            if not letters[input[lo]]:
                letters.pop(input[lo])
            lo += 1
        if len(letters) == k:
            ans.append(input[lo:hi + 1])
        hi += 1
    return ans

input = "barfoothefoobarman"
#input = "asg"
k = 10
start = time.clock()
ans =  kDistinctLetter(input, k)
print (time.clock() - start)
print len(ans)
print len(set(list(ans)))
print ans

start = time.clock()
ans = substringKdis(input, k)
print ans
print time.clock() - start