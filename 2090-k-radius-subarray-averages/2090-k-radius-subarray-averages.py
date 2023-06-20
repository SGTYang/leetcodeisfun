class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: 
            return nums
        n = len(nums)
        res = [-1 for i in range(n)]

        if k > n: 
            return res

        left, mid, right = 0, k, 2*k

        left_w = sum(nums[left:mid])
        right_w = sum(nums[mid+1: right+1])

        while right < n:
            res[mid] = (left_w + right_w + nums[mid])//(2 * k + 1)

            left_w -= nums[left]
            left += 1
            left_w += nums[mid]

            right_w -= nums[mid+1]
            right += 1
            
            if right <= len(nums)-1: 
                right_w += nums[right]

            mid += 1


        return res