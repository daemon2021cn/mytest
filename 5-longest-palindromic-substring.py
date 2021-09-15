class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        s_len = len(s)

        def findMid(seq, l, r):
            while l>=0 and r<len(seq) and seq[l] == seq[r]:
                l -= 1
                r += 1
            return seq[l+1:r]

        for i in range(s_len):
            out_mid = findMid(s, i, i)
            if len(out_mid) > len(out):
                out = out_mid

            out_mid = findMid(s, i, i+1)
            if len(out_mid) > len(out):
                out = out_mid

        return out


classNew = Solution()
s = input()
result = classNew.longestPalindrome(s)
print(result)
