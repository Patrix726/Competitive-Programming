import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.nums = []
        heapq.heapify(self.nums)
        self.added = []
        heapq.heapify(self.added)

    def popSmallest(self) -> int:
        if self.added:
            num = heapq.heappop(self.added)
            heapq.heappush(self.nums, -num)
            print(num)
            return num
        else:
            if self.nums:
                num = -heapq.heappop(self.nums)
                heapq.heappush(self.nums, -num)
                heapq.heappush(self.nums, -(num + 1))
                return num + 1
            else:
                heapq.heappush(self.nums, -1)
                return 1

    def addBack(self, num: int) -> None:
        if -num in self.nums:
            self.nums.remove(-num)
            heapq.heappush(self.added, num)
