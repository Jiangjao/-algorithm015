class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length - 1
        mid = 0 
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]