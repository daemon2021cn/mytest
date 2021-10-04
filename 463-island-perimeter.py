from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                else:
                    l = grid[i-1][j] if i-1>=0 else 0
                    r = grid[i+1][j] if i+1<=len(grid)-1 else 0
                    u = grid[i][j-1] if j-1>=0 else 0
                    b = grid[i][j+1] if j+1<=len(grid[i])-1 else 0

                    perimeter = perimeter + 4 - l - r - u - b

        return perimeter

classNew = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
results = classNew.islandPerimeter(grid)
print(results)
