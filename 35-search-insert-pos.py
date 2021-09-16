from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n_upper, n_lower = len(nums)-1, 0

        while n_upper>=n_lower: 
            n_mid = int((n_upper+n_lower+1)/2)
            if target == nums[n_mid]:
                return n_mid
            elif target > nums[n_mid]:
                n_lower = n_mid+1
            else:
                n_upper = n_mid-1
        return n_lower 

classNew = Solution()
nums=list(map(int, input().split(',')))
target = int(input())
result = classNew.searchInsert(nums, target)
print(result)
