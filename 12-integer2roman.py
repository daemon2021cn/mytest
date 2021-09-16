class Solution:
    def intToRoman(self, num: int) -> str:
        dict_r = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
        out = ""
        count = 1000

        while num:
            n_rem = num%count
            n_mod = num//count

            if n_mod == 9 or n_mod == 4:
                out += dict_r[count] + dict_r[count*(n_mod+1)]
            elif n_mod >= 5:
                out += dict_r[count*5] + dict_r[count]*(n_mod-5)
            else:
                out += dict_r[count]*n_mod

            count //= 10
            num = n_rem
        return out

        # dict_r = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
        # count = 0
        # out = ""

        # while num:
        #     carry = 10**count
        #     n_rem = num%10 * carry
        #     out_bit = ""
        #     while n_rem:
        #         for i in dict_r:
        #             if i - n_rem == carry:
        #                 out_bit = out_bit + dict_r.get(carry) + dict_r[i]
        #                 n_rem = 0
        #                 break
        #             elif i <= n_rem:
        #                 out_bit = out_bit + dict_r[i]*(n_rem//i)
        #                 n_rem -= i*(n_rem//i)
        #                 break
        #     out = out_bit+out
        #     num = num//10
        #     count += 1
        # return out

classNew = Solution()
num = int(input())
result = classNew.intToRoman(num)
print(result)
