class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l<=r:
            mid = (l+r)//2

            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            elif mid*mid >= x:
                r = mid-1
            else:
                l = mid+1

        #if x == 0 or x == 1:
        #    return x

        #for i in range(1, int(x/2)+1):
        #    if i*i <= x and (i+1)*(i+1) > x:
        #        return i


