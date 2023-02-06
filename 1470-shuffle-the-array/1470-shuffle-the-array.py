class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = 0, n
        res = []
        
        while x < n:
            res.append(nums[x])
            res.append(nums[y])
            x += 1
            y += 1
        
        return res
            