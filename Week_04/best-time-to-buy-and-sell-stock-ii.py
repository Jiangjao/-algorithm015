class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)   
        j = 0 
        count = 0
        for i in range(1,length):
            temp = prices[i] - prices[j]
            if temp > 0:
                count += temp
            j += 1
        return count