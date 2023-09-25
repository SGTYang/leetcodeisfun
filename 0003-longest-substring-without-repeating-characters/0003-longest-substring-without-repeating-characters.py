class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        curr = set()
        for right in range(len(s)):
            while curr and right > left and s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            res = max(res, len(curr))
        return res