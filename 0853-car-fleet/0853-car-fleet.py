class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        total = [[position[i], speed[i]] for i in range(len(position))]
        total.sort(reverse=True)
        
        for pos, spd in total:
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)