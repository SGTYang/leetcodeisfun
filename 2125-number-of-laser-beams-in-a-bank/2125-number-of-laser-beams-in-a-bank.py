class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_cnt = []
        res = 0
        
        for i in range(len(bank)):
            cnt = 0
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    cnt += 1
            laser_cnt.append(cnt)
            
        left, right = 0, 0
        while right < len(laser_cnt):
            if left != right and laser_cnt[right] != 0:
                res += laser_cnt[left] * laser_cnt[right]
                left = right
            
            right += 1
        
        return res        