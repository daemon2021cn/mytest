from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p_list = [('(', 1, 0)]
        res = []

        while p_list:
            p, l, r = p_list.pop()
            if l<r or l>n or r>n:
                continue
            if l==n and r==n:
                res.append(p)
            p_list.append([p+'(', l+1, r])
            p_list.append([p+')', l, r+1])
        return res

        # def generateParen(cur_p, left, right, res=[]):
        #     if left:
        #         generateParen(cur_p+'(', left-1, right)
        #     if right>left:
        #         generateParen(cur_p+')', left, right-1)
        #     if right == 0:
        #         res += cur_p, #',' will create a new list or tuple
        #     return res
        # return generateParen('', n, n)

        # out = ["()"]

        # for i in range(1,n):
        #     res = []
        #     for j in range(len(out)):
        #         for k in range(len(out[j])):
        #             res.append(out[j][:k]+"()"+out[j][k:])
        #     out = list(set(res))
        # return out

classNew = Solution()
n = int(input())
result = classNew.generateParenthesis(n)
print(result)
