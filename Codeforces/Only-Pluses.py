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
        num1, num2, num3 = invr()
        for j in range(5):
            if num1 <= num2 and num1 <= num3:
                num1 += 1
            elif num2 <= num1 and num2 <= num3:
                num2 += 1
            else:
                num3 += 1
        output.append(num1 * num2 * num3)
    for out in output:
        print(out)


execute()
