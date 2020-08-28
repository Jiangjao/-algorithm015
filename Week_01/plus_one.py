class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
         # 从最低位开始做加法运算
        length = len(digits)
        for i in range(length -1 , -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        ans = [0] * (length + 1)
        ans[0] = 1
        return ans