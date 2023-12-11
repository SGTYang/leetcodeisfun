class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_cnt = Counter(arr)
        for integer in num_cnt.keys():
            if num_cnt[integer] / len(arr) > 0.25:
                return integer