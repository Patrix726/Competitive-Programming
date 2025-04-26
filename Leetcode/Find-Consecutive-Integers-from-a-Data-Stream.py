class DataStream:

    def __init__(self, value: int, k: int):
        self.prev = None
        self.value = value
        self.count = 0
        self.k = k

    def consec(self, num: int) -> bool:
        if self.prev == num:
            self.count+=1
        else:
            self.count = 1
        if num == self.value and self.count >= self.k:
            return True
        self.prev = num
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
