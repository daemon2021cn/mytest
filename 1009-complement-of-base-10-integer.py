class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_b = bin(n)
        n_out = ""

        for i in range(2, len(n_b)):
            n_out = n_out + "1" if n_b[i] == "0" else n_out + "0"

        return int(n_out, 2)


        #import math
        #return ((2 << int(math.log(max(n, 1), 2))) - 1) ^ n
            
