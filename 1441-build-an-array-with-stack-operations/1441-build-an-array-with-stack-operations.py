class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        stack_ops = []
        idx = 0
        curr = 1
        while res != target:
            if target[idx] == curr:
                stack_ops.append("Push")
                idx += 1
                res.append(curr)
            else:
                stack_ops.append("Push")
                stack_ops.append("Pop")
            curr += 1
        return stack_ops