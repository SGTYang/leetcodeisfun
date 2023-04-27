class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            #Odd length
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
                
            #Even length
            l,r = i, i+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
        
        return res    