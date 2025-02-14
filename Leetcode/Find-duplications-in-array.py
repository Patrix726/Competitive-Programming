class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        bits = "".zfill(len(nums))
        duplicates = []
        for num in nums:
            if bits[num - 1] != "0":
                duplicates.append(num)
            else:
                bits = "".join([bits[: num - 1], "1", bits[num:]])
        return duplicates
