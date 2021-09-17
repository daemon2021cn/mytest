from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        out = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                out.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))

        return out       

classNew = Solution()
nums1 = list(map(int, input().split(',')))
nums2 = list(map(int, input().split(',')))
result = classNew.intersect(nums1, nums2)
print(result)
