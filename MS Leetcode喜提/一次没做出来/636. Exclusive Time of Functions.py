class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ret = [0]*(n)
        stack = []
        previous_time, cur_time = 0,0
        for log in logs:
            # print(ret)
            parse = log.split(":")
            if parse[1] == "start":
                if stack != []:
                    cur_time = int(parse[2])
                    ret[stack[-1]] += (cur_time - previous_time)
                    previous_time = cur_time
                stack.append(int(parse[0]))
            else:
                cur_time = int(parse[2])
                ret[stack[-1]] += (cur_time - previous_time) + 1
                previous_time = cur_time + 1
                stack.pop()
        return ret