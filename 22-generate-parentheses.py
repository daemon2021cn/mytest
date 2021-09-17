from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParen(cur_p, left, right, res=[]):
            if left:
                generateParen(cur_p+'(', left-1, right)
            if right>left:
                generateParen(cur_p+')', left, right-1)
            if right == 0:
                res += cur_p, #',' will create a new list or tuple
            return res
        return generateParen('', n, n)

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
