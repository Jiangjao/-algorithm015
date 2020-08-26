class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1 暴力
        n = len(nums)
        k = k % n
        for i in range(k):
            nums.insert(0, nums.pop())

        # 
        # 2 reverse
        def reverse(nums,l,t):
            while l < t:
                nums[l],nums[t] = nums[t], nums[l]
                l += 1
                t -= 1
            reverse(nums,0,n - 1)
            reverse(nums,0,k - 1)
            reverse(nums,k,n - 1)
