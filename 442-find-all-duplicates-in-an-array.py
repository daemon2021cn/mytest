from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []

        for i in nums:
            i = abs(i)
            if nums[i-1] < 0:
                ret.append(i)
            else:
                nums[i-1] = -nums[i-1]

        return ret


        #ret = []
        #nums.sort()

        #for i in range(1,len(nums)):
        #    if nums[i] == nums[i-1]:
        #        ret.append(nums[i])

        #return ret

classNew = Solution()
nums = list(map(int, input().split()))
results = classNew.findDuplicates(nums)
print(results)
