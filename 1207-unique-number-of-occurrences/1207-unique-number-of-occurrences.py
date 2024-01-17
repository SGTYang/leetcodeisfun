class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = defaultdict(int)
        
        for n in arr:
            cnt[n] += 1
        
        return True if len(set(cnt.values())) == len(cnt.values()) else False