import math


def expand(expr: str):
    n = expr.split("^")[1]
    n = n.strip()
    n = int(n)
    if n == 0:
        return 1

    val = expr.split("^")[0]
    val = val.strip("(")
    val = val.strip(")")
    val = val.strip()
    if "+" in val:
        expressions = val.split("+")
    elif val[0] == "-":
        expressions = val.strip("-").split("-")
    else:
        expressions = val.split("-")

    var = (
        "-" + expressions[0]
        if "+" not in val and val.startswith("-")
        else expressions[0]
    )
    var = var.strip()
    constant = expressions[-1] if "+" in val else "-" + expressions[-1]
    constant = constant.strip()
    constant = int(constant)

    if var.isdecimal():
        return (int(var) + constant) ** n
    elif constant == 0:
        coef = 1
        if len(var) > 1:
            term = var[-1]
            coef = "".join(var[:-1])
            if coef == "-":
                coef = -1
            else:
                coef = int(coef)
        return str(coef**n) + term + "^" + str(n)
    else:
        coef = 1
        term = var[-1]
        if len(var) > 1:
            coef = "".join(var[:-1])
            if coef == "-":
                coef = -1
            else:
                coef = int(coef)

        result = ""
        for i in range(n + 1):
            termPow = n - i
            coefficent = math.comb(n, i) * (coef**termPow) * (constant**i)
            if i != 0 and coefficent > 0:
                result += "+"
            if termPow == 0:
                result += str(coefficent)
                break
            if coefficent == 1:
                result += ""
            elif coefficent == -1:
                result += "-"
            else:
                result += str(coefficent)
            result += term
            result += "^" + str(termPow) if termPow != 1 else ""
        return result


print(expand("(-7x-7)^0"))
