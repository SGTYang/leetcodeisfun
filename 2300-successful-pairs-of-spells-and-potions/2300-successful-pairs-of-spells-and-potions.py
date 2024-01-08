class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        
        for i in range(len(spells)):
            potion_needed = (success + spells[i] - 1) // spells[i]
            left, right = 0, len(potions) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < potion_needed:
                    left = mid + 1
                else:
                    right = mid - 1
            
            res.append(len(potions) - left)
        
        return res