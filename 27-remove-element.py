class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[r] == val:
                r -= 1
                continue
            else:
                if nums[l] == val:
                    nums[l] = nums[r]
                    l += 1
                    r -= 1
                else:
                    l += 1

        return r+1
