# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

# Example 1:


# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.


# Example 2:


# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
 

# Constraints:

# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4

# Solution:----------------------------------------------------------------

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]
        
        # Direction arrays
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        # Add border cells to heap
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True
            
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True
            
        water = 0
        while heap:
            height, row, col = heapq.heappop(heap)
            
            for k in range(4):
                new_row, new_col = row + dx[k], col + dy[k]
                
                if (new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or 
                    visited[new_row][new_col]):
                    continue
                    
                if heightMap[new_row][new_col] < height:
                    water += height - heightMap[new_row][new_col]
                    heapq.heappush(heap, (height, new_row, new_col))
                else:
                    heapq.heappush(heap, (heightMap[new_row][new_col], new_row, new_col))
                visited[new_row][new_col] = True
                
        return water