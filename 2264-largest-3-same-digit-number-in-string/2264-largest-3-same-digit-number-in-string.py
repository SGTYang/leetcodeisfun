class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_num = -1
        
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2] and int(num[i]) > max_num:
                max_num = int(num[i])
                res = num[i:i + 3]
        
        return res