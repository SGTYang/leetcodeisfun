class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        def change(time):
            hour, minute = time.split(":")
            
            return int(hour) * 60 + int(minute)
        
        diff = change(correct) - change(current)
        
        res = 0
        
        time_increase = [60, 15, 5, 1]
        
        for time in time_increase:
            res += diff // time
            diff = diff % time
        
        return res