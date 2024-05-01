import math
def solution(a:list):
    return math.gcd(*a)*len(a)
#That's it, funny right? 
# it took you about 1 hour for this!!!!

#I will just leave this here to not waste my 1 hour
def solution2(a:list):
    i=len(a)-1
    valid = True
    while valid:
        valid = False
        while a[i]>a[i-1]:
            a[i]=a[i]-a[i-1]
            valid=True
        i=(i+1) % len(a)
    return sum(a)

