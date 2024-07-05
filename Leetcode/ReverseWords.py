def reverseWords(s: str) -> str:
    lStr = s.split()
    lStr.reverse()
    return " ".join(lStr)


print(reverseWords("   the    sky    is   blue   "))
