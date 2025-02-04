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
    count = inp()
    result = []
    for i in range(count):
        word = input().strip()
        if len(word) <= 10:
            result.append(word)
        else:
            result.append("".join([word[0], str(len(word) - 2), word[-1]]))

    for j in result:
        print(j)


execute()
