from collections import Counter
from functools import reduce


def minimumPushes(word: str) -> int:
    frequency = Counter(word)
    count = list(frequency.values())
    count.sort(reverse=True)
    keyPressed = 0
    for i in range(len(count)):
        keyPressed += count[i] * (i // 8 + 1)
    return keyPressed
