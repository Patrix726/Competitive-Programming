def calc_special(lastDigit, base):
    l = lastDigit
    rem = 0
    result = str(lastDigit)
    if base == 16 and lastDigit >= 10:
        result = str(hex(lastDigit)).lstrip("0x")
    while True:
        product = lastDigit * l + rem
        val = product % base
        rem = product // base
        if base == 16:
            result = str(hex(val)).lstrip("0x") + result if val != 0 else "0" + result
        else:
            result = str(val) + result

        l = val
        if result[0:2] == "10":
            break

    return result


print(calc_special(10, 16))
