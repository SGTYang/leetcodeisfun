class SparseVector:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.info = {}
        
        for i in range(len(nums)):
            if nums[i] != 0:
                self.info[i] = nums[i]
                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if self.size != vec.size:
            return 0
        
        res = 0
        for i in range(self.size):
            if i in self.info and i in vec.info:
                res += self.info[i] * vec.info[i]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)