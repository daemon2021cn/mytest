from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res_diff, res_sum = None, 0

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1

            while l < r:
                num_diff = nums[i] + nums[l] + nums[r] - target

                if (not res_diff) or abs(num_diff) < res_diff:
                    res_diff, res_sum = abs(num_diff), nums[i] + nums[l] + nums[r]
                if res_diff == 0:
                    break

                if num_diff > 0:
                    # while r>l:
                    #     if nums[r] == nums[r-1]:
                    #         r -= 1
                    #     else:
                    #         break
                    r -= 1
                else:
                    # while l<r:
                    #     if nums[l] == nums[l+1]:
                    #         l += 1
                    #     else:
                    #         break
                    l += 1

            if res_diff == 0:
                break

        return res_sum

classNew = Solution()
nums = list(map(int, input().split(',')))
target = int(input())
result = classNew.threeSumClosest(nums, target)
print(result)
