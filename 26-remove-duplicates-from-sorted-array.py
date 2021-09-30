from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
        return k


        #if len(nums) <= 1:
        #    return len(nums)

        #k = 0
        #for i in range(len(nums)):
        #    if nums[i] > nums[k]:
        #        k += 1
        #        nums[k], nums[i] = nums[i], nums[k]
        #        
        #return k+1

classNew = Solution()
nums = list(map(int, input().split(',')))
results = classNew.removeDuplicates(nums)
print(results)
