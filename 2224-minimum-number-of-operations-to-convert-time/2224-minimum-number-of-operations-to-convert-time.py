class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        def change(time):
            hour, minute = time.split(":")
            
            return int(hour) * 60 + int(minute)
        
        diff = change(correct) - change(current)
        
        res = 0
        
        while diff:
            if diff >= 60:
                diff -= 60
            elif diff >= 15:
                diff -= 15
            elif diff >= 5:
                diff -= 5
            else:
                diff -= 1
            res += 1
        
        return res