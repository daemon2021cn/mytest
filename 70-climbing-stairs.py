class Solution:
    def climbStairs(self, n: int) -> int:
        #Fibonacci
        steps = [1,1]

        for i in range(2, n+1):
            steps.append(steps[i-1]+steps[i-2])
        return steps[-1]

        # dp with cache
        #from functools import lru_cache
        #@lru_cache()
        #def memoryStairs(n_rem: int):
        #    if n_rem == 0:
        #        return 1 
        #    elif n_rem == 1:
        #        return memoryStairs(n_rem-1)
        #    else:
        #        return memoryStairs(n_rem-1) + memoryStairs(n_rem-2)

        #return memoryStairs(n)


classNew = Solution()
n = int(input())
result = classNew.climbStairs(n)
print(result)
