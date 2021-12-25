class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a

        a = list(map(int, [i for i in a[::-1]]))
        b = list(map(int, [i for i in b[::-1]]))
        num = 0
        result = ""
        n = len(a)

        for i in range(len(b)):
            sum_cur =  a[i]+b[i]+num if i < len(a) else b[i]+num
            if sum_cur < 2:
                num = 0
                b[i] = sum_cur
            else:
                num = 1
                b[i] = 0 if sum_cur == 2 else 1

        for i in b[::-1]:
            result += str(i)

        return result if num==0 else "1"+result


        #if num == 1:
        #    b.append(1)
        #return "".join([str(i) for i in b[::-1]])
