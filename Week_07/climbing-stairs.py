class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        tpm_list = [0,1,2]
        for i in range(3,n+1):
            tpm_list.append(tpm_list[-1]+tpm_list[-2])
        return tpm_list[-1]