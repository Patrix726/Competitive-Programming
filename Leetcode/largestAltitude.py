def largestAltitude(gain: list[int]) -> int:
    maxAlt = alt = 0
    for i in gain:
        alt += i
        if alt > maxAlt:
            maxAlt = alt
    return maxAlt


print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
