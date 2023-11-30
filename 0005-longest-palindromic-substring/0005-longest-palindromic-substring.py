class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n ^ 2)
        # Space: O(1)
        self.res = ""
        
        def is_pali(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(self.res):
                    self.res = s[l:r+1]
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # odd length
            is_pali(i, i)
            
            # even length
            is_pali(i, i + 1)
        
        return self.res
            