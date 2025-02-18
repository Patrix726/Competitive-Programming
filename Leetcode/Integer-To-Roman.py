class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_int = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        output = []
        for level, symbol in roman_to_int:
            while num >= level:
                output.append(symbol)
                num -= level
        return "".join(output)


ans = Solution()
print(ans.intToRoman(58))
