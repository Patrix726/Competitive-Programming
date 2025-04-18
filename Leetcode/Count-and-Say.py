class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s:string):
            res = ""
            cur = ""
            count = 0
            for char in s:
                if char == cur:
                    count+=1
                elif count > 0:
                    res+= str(count) + cur
                    count = 1
                else:
                    count = 1
                cur = char
            if cur and count>0:
                res+=str(count) + cur
            return res
        def recurse(n:int):
            if n==1:
                return "1"
            
            return rle(recurse(n-1))
        return recurse(n)
