class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        if rows == 0 or len(matrix[0]) == 0:
            return 0
        cols = len(matrix[0])
        # if rows == 0 or cols == 0:
        #     return 0
        dp = [[0] * cols for _ in range(rows) ]
        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                maxSide = max(maxSide,dp[i][j])
        maxSquare = maxSide * maxSide
        return maxSquare