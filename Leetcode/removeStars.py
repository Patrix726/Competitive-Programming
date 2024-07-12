def removeStars(s: str) -> str:
    arr = []

    for i in s:
        if i == "*":
            arr.pop()
        else:
            arr.append(i)
    return "".join(arr)


print(removeStars("leet**cod*e"))
