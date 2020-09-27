class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 二分查找
        length = len(matrix)
        if length == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        # 将元素映射成二维坐标
        while row < length and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False