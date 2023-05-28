class Solution:
    def frequencySort(self, s: str) -> str:
        k = len(s)
        count = defaultdict(int)
        freq = [[] for i in range(k+1)]
        res = ""
        
        for c in s:
            count[c] += 1
        
        for c, cnt in count.items():
            freq[cnt].append(c)
        
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res += n*i
        
        return res