class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        l = len(nums)
        
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            curr = nums[i]
            left,right = i+1, l-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
        
        return res