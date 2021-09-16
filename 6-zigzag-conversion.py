class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        out = [''] * numRows
        n_row, n_step = 0, 1

        for i in s:
            out[n_row] += i
            if n_row == 0:
                n_step = 1
            elif n_row == numRows -1:
                n_step = -1
            n_row += n_step

        return ''.join(out)
            
        # out = ""
        # s = list(s)
        # count = 0
        # n_row = 0

        # while s:
        #     out += s.pop(count)
        #     if count>0 and n_row>0 and count<len(s):
        #         out += s.pop(count)
        #     count = count + numRows-1 + numRows-2 - 2*n_row \
        #             if count + numRows-1 + numRows-2 - 2*n_row > 0 else 0
        #     if count >= len(s):
        #         n_row += 1
        #         count = 0

        # return out


classNew = Solution()
s = input()
numRows = int(input())
result = classNew.convert(s, numRows)
print(result)
