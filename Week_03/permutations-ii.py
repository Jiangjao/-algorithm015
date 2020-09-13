class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        visited = [False for i in range(length)]
        
        def dfs(nums,cur,result,visit):
            if len(cur) == length:
                if cur not in result:
                    result.append(cur[:])
                return
            for i in range(length):
                if visit[i]:
                    continue
                cur.append(nums[i])
                visit[i] = True
                dfs(nums, cur, result, visit)
                visit[i] = False
                cur.pop()
        dfs(nums,[],result,visited)
        return result