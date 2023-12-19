class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            0:"",
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        ans = []
        idx = 0
        while num > 0:
            rest = num % 10
            if rest not in roman:
                r = rest % 5
                q = 10 ** idx * 5 * (rest//5)
                ans.append(roman[q] + roman[10**idx] * r)
            else:
                ans.append(roman[rest*10**idx])
            
            num = num // 10
            idx += 1
        ans = ans[::-1]
        return "".join(ans)
        