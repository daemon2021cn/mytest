class Solution:
    def isPalindrome(self, x:int) -> bool:
        y = int(str(abs(x))[::-1])
        return x==y 
        #return str(x)==str(x)[::-1]

classNew = Solution()
x = int(input())
result = classNew.isPalindrome(x)
print(result)
