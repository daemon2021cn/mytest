class Solution:
    def romanToInt(self, s: str) -> int:
        dict_r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        out = 0
        s_last = dict_r[s[0]]
        for i in s:
            out = out+dict_r[i] if s_last>=dict_r[i] else out+dict_r[i]-2*s_last 
            s_last = dict_r[i]
        return out
        #dict_r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #out = 0
        #s_len = len(s)

        #for i in range(s_len):
        #    out += dict_r[s[i]]
        #    out -= (2*dict_r[s[i-1]]) if dict_r[s[i-1]]<dict_r[s[i]] and (i-1)>=0 else 0

        #return out     

classNew = Solution()
s = input()
result = classNew.romanToInt(s)
print(result)
