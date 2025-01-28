# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

# Example 1:


# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
# Example 2:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Output: 1
# Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# 0 <= grid[i][j] <= 10

# Solution:---------------------------------------------------------------------

class Solution:
    def dfs(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= nrow or j >= ncol:
            return 0
        if grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        return temp + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)

    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        nrow, ncol = len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 0:
                    res = max(res, self.dfs(grid, i, j))
        return res 