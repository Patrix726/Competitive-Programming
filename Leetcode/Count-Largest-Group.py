from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()
        max_count = 0
        for i in range(1, n+1):
            str_num = str(i)
            total = 0
            for digit in str_num:
                total += int(digit)
            count[total]+=1
            max_count = max(max_count,count[total])
        return len(list(filter(lambda x: x==max_count,count.values())))
        
        

