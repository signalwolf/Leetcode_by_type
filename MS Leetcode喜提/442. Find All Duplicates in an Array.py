def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # simple: dictionary to remember it but might over kill the problem
    # missing info, only appear once or twice, a[i] in [1, len(nums)]
    # sort and compare with index + 1 --> sort and check next
    # O(n) + O(1) solution needed

    #   [0,1,2,3,4,5,6,7]
    #   [4,3,2,7,8,2,3,1]
    # 4  7,3,2,4,8,2,3,1
    # 7  3,3,2,4,8,2,7,1
    # 3  2,3,3,4,8,2,7,1
    # 2  3,2,3,4,8,2,7,1
    # 3D D,2,3,4,8,2,7,1
    # 8  D,2,3,4,1,2,7,8
    # 1  1,2,3,4,D,2,7,8
    # 2D 1,2,3,4,D,D,7,8
    res = []
    index = 0
    lens = len(nums)
    while index != lens:
        # three case,
        # nums[index] is the expected position
        # nums[index] can be int or string
        # two action: index += 1 and swap request

        # swap condition or duplicate:
        # nums[index] != 0 and nums[index] != index + 1:
        # nums[nums[index] - 1] = nums[index] --> duplicate
        #                       !             --> swap
        # print index, nums

        if nums[index] == 0 or nums[index] == index + 1:
            index += 1
        else:
            if nums[nums[index] - 1] == nums[index]:
                res.append(nums[index])
                nums[index] = 0
                index += 1
            else:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
    print nums
    return res

alist = [3,7,2,1,3,2,1,2,1,2,6, 7]
print sorted(alist)
print sorted(findDuplicates([3,7,2,1,3,2,1,2,1,2,6, 7]))