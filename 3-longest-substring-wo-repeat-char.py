class Solution:
    def lengthnOfLongestSubstring(self, s:str) -> int:
        left, right = 0,0
        result = 0
        s_dict = {}

        while right < len(s):
            if s[right] in s_dict:
                left = max(left, s_dict[s[right]]+1)
            result = max(result, right-left+1)
            s_dict[s[right]] = right
            right += 1
        return result

        # s_tmp = []
        # s_result = 0 
        # for i in s:
        #     if i not in s_tmp:
        #         s_tmp.append(i)
        #     else:
        #         s_result = max(len(s_tmp), s_result)
        #         j = s_tmp.index(i)
        #         s_tmp = s_tmp[j+1:] if len(s_tmp) > j else s_tmp
        #         s_tmp.append(i)

        # return max(len(s_tmp), s_result)

classNew = Solution()
s = input()
result = classNew.lengthnOfLongestSubstring(s)
print(result)
