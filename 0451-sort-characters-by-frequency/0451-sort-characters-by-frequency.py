class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for i in range(len(s) + 1)]
        res = ""
        s_cnt = Counter(s)
        
        for c,f in s_cnt.items():
            buckets[f].append(c)
        
        for freq in range(len(buckets)-1, -1, -1):
            for char in buckets[freq]:
                res += char * freq
        
        return res