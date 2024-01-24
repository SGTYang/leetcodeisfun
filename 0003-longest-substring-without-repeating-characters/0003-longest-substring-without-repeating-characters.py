class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = res = 0
        curr = set()
        for right in range(len(s)):
            while left < len(s) and s[right] in curr:
                curr.remove(s[left])
                left += 1
                
            curr.add(s[right])
            
            res = max(res, len(curr))
        
        return res