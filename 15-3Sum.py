from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        out = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                num_sum = nums[l] + nums[r] + nums[i]
                if num_sum == 0:
                    out.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif num_sum < 0:
                    l += 1
                else:
                    r -= 1

        return out

        

classNew = Solution()
nums = list(map(int, input().split(',')))
result = classNew.threeSum(nums)
print(result)
