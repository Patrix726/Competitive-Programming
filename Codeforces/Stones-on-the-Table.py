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
    stones = input().strip()
    count = 0
    if n == 1:
        return 0
    for i in range(1, n):
        if stones[i] == stones[i - 1]:
            count += 1
    return count


print(execute())
