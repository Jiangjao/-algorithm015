class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        ans = 0
        for i in range(length):
            if ans >= i:
                ans = max(ans, i+ nums[i])
        if ans >= length -1:
            return True
        return False
