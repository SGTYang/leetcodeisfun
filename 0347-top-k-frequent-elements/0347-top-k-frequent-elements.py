class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        num_cnt = Counter(nums)
        res = []
        
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in num_cnt.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res