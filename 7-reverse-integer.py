class Solution:
    def reverse(self, x: int) -> int:
        # Solution-1
        y = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x:
            y = y*10 + x%10
            x //= 10
        y = y*sign
        if y > (2**31-1) or y < (- 2**31):
            y = 0
        return y
        # Solution-2
        #x_list = list(str(x))
        #x_list.reverse()
        #y = 0
        #x_len = len(x_list)

        #if x_list[-1] != '-':
        #    for i in range(x_len):
        #        y += int(x_list[x_len-1-i])*10**i
        #else:
        #    for i in range(x_len-1):
        #        y += int(x_list[x_len-2-i])*10**i
        #    y = -y

        #if y> (2**31-1) or y<-2**31:
        #    y = 0

        #return y


newClass = Solution()
x = int(input())
result = newClass.reverse(x)
print(result)
