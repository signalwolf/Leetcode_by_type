from collections import Counter


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        input_counter = Counter(nums)
        tail_tracker = Counter()
        for num in nums:

            if input_counter[num] == 0: continue

            if tail_tracker[num] > 0:
                tail_tracker[num] -= 1
                tail_tracker[num + 1] += 1
                input_counter[num] -= 1
            else:
                if input_counter[num + 1] > 0 and input_counter[num + 2] > 0:
                    input_counter[num] -= 1
                    input_counter[num + 1] -= 1
                    input_counter[num + 2] -= 1
                    tail_tracker[num + 3] += 1
                else:
                    return False
        return True