def maxVowels(s: str, k: int) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    num = maxNum = len(list(filter(lambda x: x in vowels, s[:k])))
    for i in range(k, len(s)):
        if s[i] in vowels:
            num += 1
        if s[i - k] in vowels:
            num -= 1
        maxNum = max(maxNum, num)

    return maxNum


print(maxVowels("aeiou", 2))
