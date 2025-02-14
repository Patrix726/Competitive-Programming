from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        if self.nums[number] in self.freq:
            self.reduceOrRemove(self.nums[number])
        self.nums[number] += 1
        self.freq[self.nums[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.nums[number] > 0:
            self.reduceOrRemove(self.nums[number])
            self.nums[number] -= 1
            self.freq[self.nums[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq

    def reduceOrRemove(self, frequency: int):
        freq = self.freq[frequency]
        if freq > 1:
            self.freq[frequency] -= 1
        else:
            self.freq.pop(frequency)


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
