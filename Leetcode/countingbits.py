def countBits(n: int) -> list[int]:
    return [bin(x).count("1") for x in range(n + 1)]


print(countBits(5))
