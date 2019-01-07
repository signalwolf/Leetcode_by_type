def helper(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    return len(stack)

def dfs(s, steps, left, right):
    print steps, s, left, right
    if steps == 0:
        return s
    else:
        if left >= right:
            left -= 1
            target = '('
        else:
            right -= 1
            target = ')'

        seen = set()
        for index, char in enumerate(s):
            if char == target:
                newS = s[:index] + s[index + 1:]
                if newS not in seen and helper(newS) == steps - 1:
                    seen.add(newS)
                    result = dfs(newS, steps - 1, left, right)
                    if result:
                        return result
        return



def validate(s):
    steps = helper(s)
    return dfs(s, steps, s.count('('), s.count(')'))

s = '())(()()'
print validate(s)
