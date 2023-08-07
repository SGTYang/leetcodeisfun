class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = (total) // 2
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            a_left = nums1[i] if i >= 0 else float('-inf')
            a_right = nums1[i + 1] if i + 1 < len(nums1) else float('inf')
            b_left = nums2[j] if j >= 0 else float('-inf')
            b_right = nums2[j + 1] if j + 1 < len(nums2) else float('inf')
            
            if a_left <= b_right and b_left < a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1