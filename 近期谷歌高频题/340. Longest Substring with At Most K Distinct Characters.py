from random import randint
def longestStringwithKdistictChar(s, k):
    # special handle:
    if k == 0: return 0
    if len(s) <= k: return len(s)
    left, right = 0, 1
    lens = len(s)
    position = {s[left]:0}
    # heap = [[0, s[left]]]
    ans = 0
    while left + k < lens:
        if right < lens and s[right] in position:
            position[s[right]] = right
            right += 1
        elif right < lens and s[right] not in position and len(position) < k:
            position[s[right]] = right
            right += 1
        else:
            ans = max(ans, right - left)
            potention_p, potention_char = float('inf'), None
            for char, p in position.items():
                if p < potention_p:
                    potention_p, potention_char = p, char
            left = potention_p + 1
            del position[potention_char]
    return ans

char = 'dasdedwivxk'
k = randint(1, len(char))
k = 5
print k, len(char), len(set(char))
print longestStringwithKdistictChar(char, k)
