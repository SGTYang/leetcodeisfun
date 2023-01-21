class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        m, n = len(nums1), len(nums2)
        num1_pointer = num2_pointer = 0
        
        while num1_pointer < m-1 and num2_pointer < n-1 and nums1[num1_pointer] != nums2[num2_pointer]:
            if nums1[num1_pointer] < nums2[num2_pointer]:
                num1_pointer += 1
            else:
                num2_pointer += 1
        
        if nums1[num1_pointer] == nums2[num2_pointer]:
            return nums1[num1_pointer]
        else:
            return -1