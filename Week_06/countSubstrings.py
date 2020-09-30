class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划，最小子问题是??
        # dp[i][j] ==1 or 2其他时都要判断
        count = 0
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        for j in range(length):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = True
                    count += 1
                elif j - i == 1 and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
                elif j - i > 1 and s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        return count