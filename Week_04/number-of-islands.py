class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        count = 0
        def dfs(grid, i ,j):
            if not 0 <= i < length or not  0 <= j < len(grid[0]) or grid[i][j]=='0':return 
            grid[i][j] = '0'
            dfs(grid, i - 1,j)
            dfs(grid, i + 1,j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j -1)
        for i in range(length):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count