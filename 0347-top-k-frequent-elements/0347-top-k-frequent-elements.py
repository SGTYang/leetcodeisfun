class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums))]
        res = []
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        for k_,v in num_count.items():
            bucket[v-1].append(k_)
        
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return None