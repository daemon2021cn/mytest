class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        while n > m:
            m <<= 1
        return n==m

        # return n>0 and n&(n-1)==0
