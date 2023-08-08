class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        half = total // 2
        
        l, r = 0, l1 - 1
        while True:
            mid = (l + r) // 2
            rest = half - mid - 2
            
            nums1_left = nums1[mid] if mid >= 0 else float('-inf')
            nums1_right = nums1[mid + 1] if mid + 1 < len(nums1) else float('inf')
            nums2_left = nums2[rest] if rest >= 0 else float('-inf')
            nums2_right = nums2[rest + 1] if rest + 1 < len(nums2) else float('inf')
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                r = mid - 1
            else:
                l = mid + 1
        