class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        
        for i in range(len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                return True
            
        
        return False
                    
                    