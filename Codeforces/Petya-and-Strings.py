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
    word1 = input().strip().lower()
    word2 = input().strip().lower()
    if word1 < word2:
        return "-1"
    elif word1 > word2:
        return "1"
    else:
        return "0"


print(execute())
