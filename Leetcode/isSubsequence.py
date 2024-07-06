def isSubsequence(s: str, t: str) -> bool:
    cur = 0
    length = len(s)
    if length == 0:
        return True
    for i in t:
        if s[cur] == i:
            cur += 1
        if cur == length:
            return True
    return False


print(isSubsequence("axc", "ahbgdc"))
