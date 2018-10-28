
def helper(ranges, curr_start, curr_end, target_range, visited):
    if (curr_start, curr_end) in visited:
        return False

    if curr_start >= target_range[0] and curr_end <= target_range[1]:
        return True

    elif curr_end > target_range[1]:
        return False

    else:
        for range in ranges:
            start, end = range
            ns, ne = start + curr_start, end + curr_end
            if helper(ranges, ns, ne, target_range, visited):
                return True

        visited.add((curr_start, curr_end))
        return False


def validation_coke_machine (ranges, target_range):
    # ranges change to set
    # target_range save to visited
    # target_range keep reduce
    # check reduced target ranges in ranges or not?
    visited = set()
    res = helper(ranges, 0, 0, target_range, visited)
    print visited
    return res

ranges = [[100, 120], [200, 240], [400, 410]]
target = [ranges[0][0] * 5 + ranges[2][0]*3, ranges[0][1] * 5 + ranges[2][1]*3]
print validation_coke_machine(ranges, target)