class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits[0] += 1
        addition = (digits[0]) // 10
        digits[0] = digits[0] % 10
        
        
        for i in range(1, len(digits)):
            if addition:
                digits[i] += 1
                addition = digits[i] // 10
                digits[i] = digits[i] % 10
        
        if addition:
            digits.append(1)
        digits.reverse()
        return digits