class Solution:
    def findComplement(self, num: int) -> int:
        num_bit = len(bin(num))-2
        return num^(2**num_bit-1)
