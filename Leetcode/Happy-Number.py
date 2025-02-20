class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            new_n = sum([int(i) ** 2 for i in str(n)])
            if new_n in nums:
                return False
            else:
                n = new_n
                nums.add(n)
        return True
