from collections import defaultdict
from math import factorial

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        domino_count = defaultdict(int)
        for i,j in dominoes:
            if (j,i) in domino_count:
                domino_count[(j,i)]+=1
            else:
                domino_count[(i,j)]+=1
        total = 0
        for value in domino_count.values():
            if value >= 2:
                total+= factorial(value)//(2*factorial(value-2))
        return total
            

