class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sum, sum_val = nums[0], 0

        for i in nums:
            sum_val += i
            sum = max(sum_val, sum)
            sum_val = max(0, sum_val)

        return sum

        #DP
        # dp = [0]*len(nums)
        # for i in range(len(nums)):
        #     dp[i] = max(nums[i], dp[i-1]+nums[i])
        # return max(dp)
