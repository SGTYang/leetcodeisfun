class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        res = []
        res.append([n for n in set1 if n not in set2])
        res.append([n for n in set2 if n not in set1])
        return res