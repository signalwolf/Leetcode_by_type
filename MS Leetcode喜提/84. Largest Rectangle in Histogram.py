class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0: return 0
        # calculate the left
        left = [0] * len(heights)
        stack = []
        for i, val in enumerate(heights):
            if i == 0:
                stack.append([val, i])
                continue

            if heights[i] > heights[i - 1]:
                left[i] = 0
                stack.append([val, i])

            if heights[i] == heights[i - 1]:
                left[i] = left[i - 1] + 1

            if heights[i] < heights[i - 1]:
                while stack and stack[-1][0] >= val:
                    _, prev_index = stack.pop()
                left[i] = left[prev_index] + i - prev_index
                stack.append([val, i])

        # calculate the right
        right = [0] * len(heights)
        stack = []
        for i in xrange(len(heights) - 1, -1, -1):
            val = heights[i]
            if i == len(heights) - 1:
                stack.append([val, i])
                continue

            if heights[i] > heights[i + 1]:
                right[i] = 0
                stack.append([val, i])

            if heights[i] == heights[i + 1]:
                right[i] = right[i + 1] + 1

            if heights[i] < heights[i + 1]:
                while stack and stack[-1][0] >= val:
                    _, prev_index = stack.pop()
                right[i] = right[prev_index] + prev_index - i
                stack.append([val, i])

        # calculate the ans:
        ans = [0] * len(heights)
        for i in xrange(len(heights)):
            ans[i] = ((left[i] + right[i]) + 1) * heights[i]

        return max(ans)