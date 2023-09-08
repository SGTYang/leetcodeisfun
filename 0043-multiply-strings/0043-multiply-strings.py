class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_dict = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }
        total = 0
        digit_1 = 0
        for i in range(len(num1)-1, -1, -1):
            digit_2 = 0
            curr = 0
            for j in range(len(num2)-1, -1, -1):
                curr += num_dict[num1[i]] * num_dict[num2[j]] * 10**digit_2
                digit_2 += 1
            total += curr * 10**digit_1
            digit_1 += 1
        
        return str(total)