def decodeString(s: str) -> str:
    strings = []
    mult = []
    ind = 0
    output = ""
    while ind < len(s):
        val = s[ind]
        if val.isdigit():
            if strings and len(mult) <= len(strings):
                strings[-1][1] += s[strings[-1][0] : ind]
            if len(mult) > len(strings):
                mult[-1] += val
            else:
                mult.append(val)
        elif val == "[":
            strings.append([ind + 1, ""])
        elif val == "]":
            string = strings.pop()
            mul = int(mult.pop())
            if strings:
                strings[-1][1] += mul * (string[1] + s[string[0] : ind])
                strings[-1][0] = ind + 1
            else:
                # output += mul * string[1] if string[1] else mul * s[string[0] : ind]
                output += mul * (string[1] + s[string[0] : ind])
        elif strings == []:
            output += val

        ind += 1
    return output


print(decodeString("1[a1[b1[c]d]s]"))
