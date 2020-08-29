class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                continue
        while j < length:
            nums[j] = 0
            j += 1