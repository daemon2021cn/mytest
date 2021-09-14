from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution-1: O(n^2) time complexity
        #len_n = len(nums)
        #for i in range(len_n):
        #    for j in range(i+1, len_n):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]

        #solution-2: O(n) time complexity
        dict_n = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dict_n:
                return [dict_n[diff], i]

            dict_n[nums[i]] = i

newc = Solution()
nums = list(map(int, input().split(',')))
target = int(input())
result = newc.twoSum(nums, target)
print(result)
