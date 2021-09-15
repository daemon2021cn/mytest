from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                out += char[0]
            else:
                return out
        return out

        # s_len = len(strs)
        # out = ""
        # s_len_min = 0

        # for i in range(s_len):
        #     if len(strs[i]) == 0:
        #         return out
        #     s_len_min = min(len(strs[i]), s_len_min) if s_len_min != 0 else len(strs[i])

        # for k in range(s_len_min):
        #     tmp = strs[0][k]
        #     for i in range(s_len):
        #         if tmp == strs[i][k]:
        #             continue
        #         else:
        #             return out
        #     out += tmp

        # return out
                

classNew = Solution()
strs = [i for i in input().split(',')]
result = classNew.longestCommonPrefix(strs)
print(result)
