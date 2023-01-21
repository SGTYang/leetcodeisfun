class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        if k == 0 :
            if nums1 != nums2:
                return -1 
            else:
                return 0
    
        neg = pos = 0
        
        l = len(nums1)
        
        for i in range(l):
            diff = nums1[i]-nums2[i]
            if abs(diff) % k != 0:
                return -1
            if diff < 0:
                neg += diff
            elif diff > 0:
                pos += diff
        
        if neg + pos == 0:
            return pos//k
        return -1