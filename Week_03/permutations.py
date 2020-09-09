class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length <= 1:
            return [nums]
        result = []
        visit = [False for _ in range(length)]
        def dfs(numbers, cur, result, visit):
            if len(cur) == length:
                result.append(cur[:])
                return
            for i in range(length):
                if visit[i]:
                    continue
                cur.append(numbers[i])
                visit[i] = True
                dfs(numbers, cur, result, visit)
                visit[i] =  False
                cur.pop()
        dfs(nums, [], result, visit)
        return result