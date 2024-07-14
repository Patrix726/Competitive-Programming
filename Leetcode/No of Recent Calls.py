class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        length = len(self.requests)
        for i in range(length):
            if self.requests[i] < t - 3000:
                length -= 1
            else:
                self.requests = self.requests[i:]
                break
        return length


# Your RecentCounter object will be instantiated and called as such:

obj = RecentCounter()
param_1 = obj.ping(1)
