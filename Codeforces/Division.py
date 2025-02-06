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
    n = inp()
    output = []
    for i in range(n):
        rating = inp()
        if rating <= 1399:
            output.append("Division 4")
        elif rating <= 1599:
            output.append("Division 3")
        elif rating <= 1899:
            output.append("Division 2")
        else:
            output.append("Division 1")
    for result in output:
        print(result)


execute()
