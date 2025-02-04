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
    solutions = 0
    for i in range(count):
        vote = list(invr())
        if vote.count(1) >= 2:
            solutions += 1
    print(solutions)


execute()
