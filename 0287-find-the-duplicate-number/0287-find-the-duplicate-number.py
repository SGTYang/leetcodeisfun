class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 2(p+c-x) = p+nc-x
        slow, fast = 0, 0
        
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while 1:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow