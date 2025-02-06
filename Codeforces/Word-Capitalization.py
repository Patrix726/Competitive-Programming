import sys

input = sys.stdin.readline


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def execute():
    word = input().strip()
    if len(word) == 1:
        return word.upper()
    return "".join([word[0].upper(), word[1:]])


print(execute())
