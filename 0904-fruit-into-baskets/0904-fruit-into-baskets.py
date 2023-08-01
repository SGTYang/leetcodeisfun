class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        res = 0
        total = 0
        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            total += 1
            while len(basket) > 2:
                curr = fruits[left]
                basket[curr] -= 1
                total -= 1
                if basket[curr] == 0:
                    basket.pop(curr)
                left += 1
            res = max(res, total)
        
        return res