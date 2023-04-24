class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r,l = 0, len(nums)-1
        res = []
        while r <= l:
            if nums[r]*nums[r] < nums[l]*nums[l]:
                res.append(nums[l]*nums[l])
                l -= 1
            else:
                res.append(nums[r]*nums[r])
                r += 1
        
        return res[::-1]