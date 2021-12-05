from typing import List
from functools import reduce
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict_d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return reduce(lambda pre, digit_cur: [x+y for x in pre for y in dict_d[digit_cur]], digits, [''])



        # if not digits:
        #     return []
        # dict_d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        # if len(digits) == 1:
        #     return list(dict_d[digits])

        # digits_pre = self.letterCombinations(digits[:-1])
        # digits_cur = list(dict_d[digits[-1]])
        # return [pre+cur for pre in digits_pre for cur in digits_cur]



        # if not digits:
        #     return []

        # dict_d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # ret = []
        # for i in digits:
        #     if not ret:
        #         for j in dict_d[i]:
        #             ret.append(j)
        #     else:
        #         ret_tmp = []
        #         for j in dict_d[i]:
        #             for k in ret:
        #                 ret_tmp.append(k+j)
        #         ret = ret_tmp

        # return ret

classNew = Solution()
digits = input()
results = classNew.letterCombinations(digits)
print(results)
