class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

        # if not needle:
        #     return 0

        # j, start = 0, -1
        # n_len = len(neelde)
        # for i,val in enumerate(haystack):
        #     if val==needle[j]:
        #         start = i if j == 0 else start
        #         j += 1
        #         if j == n_len:
        #             return start 
        #     elif j>0:
        #         j, start = 0, -1

        # return start 

        #return haystack.find(needle)

classNew = Solution()
haystack = input()
needle = input()
result = classNew.strStr(haystack, needle)
print(result)
