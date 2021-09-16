class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        out = 0
        if not s:
            return 0
        sign = -1 if s[0]=='-' else 1
        
        if s[0] == '+' or s[0] == '-':
            s = s[1:] if len(s)>1 else ''

        for j in s:
            if not j.isdigit():
                break
            else:
                out = out*10+ord(j)-ord('0')
        out = out*sign

        return min(max(out, -(2**31)), 2**31-1)

        # if not s:
        #     return 0

        # sign = 1
        # n_max, n_min = 2**31-1, -(2**31)
        # out = ""
        # count = 0

        # for i in s:
        #     if i == ' ' and out == "" and count==0:
        #         continue

        #     if (i == '+' or i == '-') and count == 0 and out=="":
        #         count += 1
        #         sign = 1 if i == '+' else -1
        #         continue
        #         
        #     if i.isdigit():
        #         out += i
        #         continue
        #     elif out:
        #         break
        #     else:
        #         return 0
        # if out == "":
        #     return 0

        # result = int(out)*sign
        # result = n_max if result>n_max else n_min if result<n_min else result

        # return result


classNew = Solution()
s = input()
result = classNew.myAtoi(s)
print(result)
