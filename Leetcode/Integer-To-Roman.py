class Solution:
    def intToRoman(self, num: int) -> str:
        output = []
        output.extend(["M" for i in range(num//1000)])
        num = num%1000
        if num>=900:
            output.append("CM")
            num %=900
        elif num>=500:
            output.append("D")
            num %=500
        elif num >= 400:
            output.append("CD")
            num %=400
        output.extend(["C" for i in range(num//100)])
        num%=100
        
        if num>=90:
            output.append("XC")
            num %=90
        elif num>=50:
            output.append("L")
            num %=50
        elif num>=40:
            output.append("XL")
            num %=40
        output.extend(["X" for i in range(num//10)])
        num%=10
        if num==9:
            output.append("IX")
        elif num>=5:
            output.append("V")
            output.extend(["I" for i in range(num%5)])
        elif num==4:
            output.append("IV")
        else:
            output.extend(["I" for i in range(num)])
        return "".join(output)
        


