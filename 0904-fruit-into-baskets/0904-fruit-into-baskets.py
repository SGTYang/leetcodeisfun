class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        buckets = defaultdict(int)
        left = res = 0
        for i in range(len(fruits)):
            buckets[fruits[i]] += 1
            
            while len(buckets)>2:
                f = fruits[left]
                buckets[f] -= 1
                left += 1
                if not buckets[f]:
                    buckets.pop(f)

            res = max(res, sum(buckets.values()))

        return res