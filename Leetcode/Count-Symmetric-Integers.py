class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0
        for i in range(low, high+1):
            str_num = str(i)
            n = len(str_num)
            if n % 2 != 0:
                continue
            if sum(map(int,str_num[:n//2])) == sum(map(int, str_num[n//2:])):
                output+=1
        return output
