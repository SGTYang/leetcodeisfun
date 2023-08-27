class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dp(stones):
            A = [[0] * len(stones) for _ in range(len(stones))]
            if stones[1] == 1:
                A[1][1] = 1
                
            for i in range(2, len(stones)):
                for j in range(1, i):
                    k = stones[i] - stones[j]
                    if 0 < k <= i:
                        left = mid = right = 0
                        if k - 1 >= 0:
                            left = A[j][k - 1]
                        mid = A[j][k]
                        if k + 1 < len(stones):
                            right = A[j][k + 1]
                        A[i][k] = left or mid or right

            for i in range(len(A)):
                if A[-1][i]:
                    return True
                
            return False  
        return dp(stones)