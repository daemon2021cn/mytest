class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(':')', '[':']', '{':'}'}
        s_rem = []

        for i in s:
            if i in match:
                s_rem.append(i)
            elif not (len(s_rem)>0 and match[s_rem.pop(-1)] == i):
                return False
        return len(s_rem)==0
        # s_rem = []
        # b_left = {'(':0, '[':1, '{':2}
        # b_right = {')':0, ']':1, '}':2}

        # for i in s:
        #     if i in b_left:
        #         s_rem.append(i)
        #     else:
        #         if s_rem:
        #             if s_rem[-1] in b_left and b_left[s_rem[-1]] == b_right[i]:
        #                 s_rem.pop(-1)
        #             else:
        #                 return False
        #         else:
        #             return False

        # if s_rem:
        #     return False
        # return True


classNew = Solution()
s = input()
result = classNew.isValid(s)
print(result)
