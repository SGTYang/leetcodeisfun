class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, total, res = 0, 0, 0
        basket = defaultdict(int)
        
        for i in range(len(fruits)):
            basket[fruits[i]] += 1
            total += 1
            while len(basket) > 2:
                curr = fruits[left]
                basket[curr] -= 1
                total -= 1
                left += 1
                if basket[curr] == 0:
                    basket.pop(curr)
                
            res = max(res, total)
        
        return res