class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        res = []
        rows = len(nums)
        
        for i in range(rows - 1, - 1, -1):
            for j in range(len(nums[i])):
                diagonal = i + j
                groups[diagonal].append(nums[i][j])
        
        curr = 0
        while curr in groups:
            res.extend(groups[curr])
            curr += 1
        
        return res