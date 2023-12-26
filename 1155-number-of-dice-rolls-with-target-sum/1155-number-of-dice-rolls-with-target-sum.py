class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}

        def getRoll(current_sum, dices):
            if (current_sum, dices) in dp:
                return dp[(current_sum,dices)]
            if current_sum > target:
                return 0
            if dices == 0:
                return 1 if current_sum == target else 0
            
            total_sum = (sum([getRoll(current_sum+i, dices-1) for i in range(1,k+1)]))%(10**9+7)
            dp[(current_sum, dices)] = total_sum
            return total_sum
        
        print(dp)
        return getRoll(0, n)