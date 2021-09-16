from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, width, area = 0, len(height)-1, len(height)-1, 0

        for i in range(width, 0, -1):
            if height[l] < height[r]:
                area, l = max(area, i*height[l]), l+1
            else:
                area, r = max(area, i*height[r]), r-1
        return area

classNew = Solution()
height = list(map(int, input().split(',')))
result = classNew.maxArea(height)
print(result)
