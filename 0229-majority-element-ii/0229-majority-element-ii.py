class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(int)
        comp = len(nums)/3
        res = []
        
        for num in nums:
            nums_dict[num] += 1
        for num, cnt in nums_dict.items():
            if cnt > comp:
                res.append(num)
        
        return res