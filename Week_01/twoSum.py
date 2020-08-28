class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # length = len(nums)
        # for i in range(length-1):
        #     for j in range(1,length):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]

        # 字典的特性
        d = {}
        length = len(nums)
        for x in range(length):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x