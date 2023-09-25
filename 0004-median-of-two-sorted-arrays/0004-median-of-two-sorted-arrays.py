class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        half = total // 2
        
        left, right = 0, l1 - 1
        while True:
            mid = (left + right) // 2
            idx = half - mid - 2
            
            nums1_left = nums1[mid] if mid >=0 else float('-inf')
            nums1_right = nums1[mid + 1] if mid + 1 < len(nums1) else float('inf')
            nums2_left = nums2[idx] if idx >= 0 else float('-inf')
            nums2_right = nums2[idx + 1] if idx + 1 < len(nums2) else float('inf')
            
            if nums1_left <= nums2_right and nums1_right >= nums2_left:
                if total % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums2_right, nums1_right)) / 2
            elif nums1_left > nums2_right:
                right = mid - 1
            else:
                left = mid + 1