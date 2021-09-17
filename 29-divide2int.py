class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        sign = (((dividend<0) != (divisor<0)))
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            divisor_cur = divisor
            i = 1
            while dividend >= divisor_cur:
                dividend -= divisor_cur
                res += i
                i <<= 1
                divisor_cur <<= 1

        if sign:
            res = -res
        return min(max(res, -2**31),2**31-1)


        # if dividend == 0:
        #     return 0

        # dividend,divisor = str(dividend), str(divisor)
        # sign_d, sign_r = 1, 1

        # if dividend[0] == '-':
        #     sign_d = -1
        #     dividend = dividend[1:]

        # if divisor[0] == '-':
        #     sign_r = -1
        #     divisor = divisor[1:]

        # sign = '-' if sign_d != sign_r else '+'
        # divisor = int(divisor)
        # 
        # res = ""
        # carry = ''

        # for i in dividend:
        #     d_bit = int(carry+i)
        #     d_sum = 0
        #     while d_bit:
        #         if d_bit >= divisor:
        #             d_bit -= divisor
        #             d_sum += 1
        #         else:
        #             break
        #     res += str(d_sum)
        #     carry = str(d_bit)

        # return min(max(int(sign+res), -2**31), 2**31-1)

classNew = Solution()
dividend = int(input())
divisor = int(input())
result = classNew.divide(dividend, divisor)
print(result)
