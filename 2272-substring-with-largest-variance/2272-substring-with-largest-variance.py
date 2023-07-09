class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0 
        seen = set(s)
        for x in ascii_lowercase: 
            for y in ascii_lowercase: 
                if x != y and x in seen and y in seen: 
                    vals = []
                    for ch in s: 
                        if ch == x: vals.append(1)
                        elif ch == y: vals.append(-1)
                    cand = prefix = least = 0 
                    ii = -1 
                    for i, v in enumerate(vals): 
                        prefix += v
                        if prefix < least: 
                            least = prefix 
                            ii = i 
                        ans = max(ans, min(prefix-least, i-ii-1))
        return ans 