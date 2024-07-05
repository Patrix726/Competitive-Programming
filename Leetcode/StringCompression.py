def compress(chars: list[str]) -> int:
    curChar = ""
    count = 0
    s = ""
    charsCopy = chars.copy()
    chars.clear()
    for i in charsCopy:
        if i == curChar:
            count += 1
        else:
            if count == 1:
                s += curChar
                chars.append(curChar)
                count = 1
            elif count > 1:
                s += curChar + str(count)
                chars.append(curChar)
                if count < 10:
                    chars.append(str(count))
                else:
                    for j in str(count):
                        chars.append(j)
                count = 1
            else:
                count += 1
            curChar = i

    if count == 1:
        s += curChar
        chars.append(curChar)
    elif count > 1:
        s += curChar + str(count)
        chars.append(curChar)
        if count < 10:
            chars.append(str(count))
        else:
            for j in str(count):
                chars.append(j)
    print(chars)
    return len(s)


print(compress(["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
