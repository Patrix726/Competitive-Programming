from math import factorial
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        output = []
        for i in range(rowIndex+1):
            value = factorial(rowIndex)//(factorial(i)*factorial(rowIndex-i))
            output.append(value)
        return output
