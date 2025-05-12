from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        count = Counter(digits)
        output = []
        for num in range(100,1000,2):
            l = num // 100
            m = (num % 100) // 10
            r = num % 10

            num_count = Counter([l,m,r])
            valid = True
            for k,v in num_count.items():
                if v > count[k]:
                    valid = False
            if valid:
                output.append(num)
        return output

        
