class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ##dynamic programming
        #dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

        #text1 = " " + text1
        #text2 = " " + text2

        #for i in range(1,len(text1)):
        #    for j in range(1,len(text2)):
        #        if text1[i] == text2[j]:
        #            dp[i][j] = 1 + dp[i-1][j-1]
        #        else:
        #            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        #return dp[-1][-1]

        #DP with least recently used cache
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def memory_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0

            if text1[ptr1] == text2[ptr2]:
                return 1+memory_solve(ptr1+1, ptr2+1)
            else:
                return max(memory_solve(ptr1+1, ptr2), memory_solve(ptr1, ptr2+1))

        return memory_solve(0,0)


classNew = Solution()
text1 = input()
text2 = input()
results = classNew.longestCommonSubsequence(text1, text2)
print(results)
