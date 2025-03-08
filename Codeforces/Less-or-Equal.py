from collections import Counter
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
    _, k = invr()
    nums = inlt()
    nums.sort()
    nums_count = list(Counter(nums).items())
    total = 0
    ind = 0
    if k==0:
        x = nums_count[ind][0]-1
        return x if x >= 1 else -1
    while total < k and ind < len(nums_count):
        total+= nums_count[ind][1]
        if total == k:
            return nums_count[ind][0]
        ind+=1
    return -1
print(execute())
