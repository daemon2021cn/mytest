from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = []
        self.numSumTarget(nums, 4, target, [], ret)
        return ret

    def numSumTarget(self, nums, N, target, ret_cur, ret):
        if len(nums) < N or N < 2:
            return

        if N == 2:
            l, r = 0, len(nums)-1

            while l<r:
                num_sum = nums[l] + nums[r]
                if num_sum == target:
                    ret.append(ret_cur+[nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                    while r>l and nums[r]==nums[r+1]:
                        r -= 1
                elif num_sum < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    self.numSumTarget(nums[i+1:], N-1, target-nums[i], ret_cur+[nums[i]], ret)
        return


        # if len(nums) < 4:
        #     return []

        # nums.sort()
        # ret = []
        # 
        # for i in range(len(nums)-3):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue

        #     for j in range(i+1, len(nums)-2):
        #         if j>i+1 and nums[j] == nums[j-1]:
        #             continue

        #         l, r = j+1, len(nums)-1

        #         while l<r:
        #             sum_nums = nums[i] + nums[j] + nums[l] + nums[r]

        #             if sum_nums == target:
        #                 ret.append([nums[i], nums[j], nums[l], nums[r]])

        #             if sum_nums < target:
        #                 while l<r and nums[l] == nums[l+1]:
        #                     l += 1
        #                 l += 1
        #             elif sum_nums > target:
        #                 while r>l and nums[r] == nums[r-1]:
        #                     r -= 1
        #                 r -= 1
        #             else:
        #                 while l<r and nums[l] == nums[l+1]:
        #                     l += 1
        #                 while r>l and nums[r] == nums[r-1]:
        #                     r -= 1
        #                 l += 1
        #                 r -= 1
        #                                        
        # return ret




classNew = Solution()
nums = list(map(int, input().split(',')))
target = int(input())
results = classNew.fourSum(nums, target)
print(results)
