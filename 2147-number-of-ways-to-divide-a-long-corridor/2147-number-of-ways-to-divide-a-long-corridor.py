class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seat_cnt = 0
        last_idx = -1
        
        res = 1
        for i, c in enumerate(corridor):
            if c == "S":
                seat_cnt += 1

                if seat_cnt == 2:
                    last_idx = i
                    seat_cnt = 0
                
                elif seat_cnt == 1 and last_idx != -1:
                    res = (res * (i - last_idx)) % MOD
        
        if seat_cnt == 1 or last_idx == -1:
            return 0
        
        return res
        
        
        MOD = 10**9 + 7
        dp = {}
        
        def count(idx, seats):
            if idx == len(corridor):
                return 1 if seats == 2 else 0
            
            if (idx, seats) in dp:
                return dp[(idx, seats)]
            
            if seats == 2:
                if corridor[idx] == "S":
                    res = count(idx + 1, 1)
                else:
                    res = (count(idx + 1, 0) + count(idx + 1, 2)) % MOD
            else:
                if corridor[idx] == "S":
                    res = count(idx + 1, seats + 1)
                else:
                    res = count(idx + 1, seats)
            
            dp[(idx, seats)] = res
            return dp[(idx, seats)]
        
        return count(0, 0)