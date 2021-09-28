from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ret_e, ret_o, ret = [], [], []
        for i in range(len(nums)):
            if nums[i]%2==0:
                ret_e.append(nums[i])
            else:
                ret_o.append(nums[i])
            if ret_e and ret_o:
                ret.append(ret_e.pop())
                ret.append(ret_o.pop())

        return ret

classNew = Solution()
nums = list(map(int, input().split(',')))
results = classNew.sortArrayByParityII(nums)
print(results)
