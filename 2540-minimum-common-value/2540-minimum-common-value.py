class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1_set = set(nums1)
        
        for n in nums2:
            if n in nums1_set:
                return n
        return -1