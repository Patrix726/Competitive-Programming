
from collections import defaultdict

class TimeMap:

    def __init__(self):
        
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        
        n = len(self.store[key])
        left = 0
        right = n - 1

        if n == 0 or self.store[key][left][1] > timestamp:
            return ""

        while left < right:
            mid = (left + right)//2
            if self.store[key][mid][1] == timestamp:
                return self.store[key][mid][0]
            elif self.store[key][mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return self.store[key][left][0] if left < n and self.store[key][left][1] <= timestamp else self.store[key][left-1][0]

