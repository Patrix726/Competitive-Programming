import math


def convertToInt(x, y):
    lenX = len(x)
    lenY = len(y)
    maxLen = max(lenX, lenY)
    minLen = min(lenX, lenY)
    num = math.ceil(maxLen / 4200)
    parts = []
    carry = 0
    for i in range(num):
        intX = 0
        intY = 0
        xNum = 4200 if lenX >= 4200 else lenX
        yNum = 4200 if lenY >= 4200 else lenY
        if lenX != 0:
            strX = x[lenX - xNum : lenX]
            intX = int(strX)
        if lenY != 0:
            strY = y[lenY - yNum : lenY]
            intY = int(strY)
        sum = intX + intY + carry
        strSum = str(sum)
        if len(strSum) > 4200:
            carry = int(strSum[0])
            parts.append(strSum[1:])
        else:
            carry = 0
            parts.append(strSum)
        lenX -= xNum
        lenY -= yNum
    if carry != 0:
        parts.append(str(carry))
    return parts


def sum_strings(x, y):
    if x == y == "":
        return "0"
    arr = convertToInt(x, y)
    stringSum = ""
    divmod()
    for i in arr:
        stringSum = i + stringSum
    return stringSum


print(sum_strings("99", "3"))
