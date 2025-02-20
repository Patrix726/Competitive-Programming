class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        nums_in_int = [int(binary_num, 2) for binary_num in nums]
        entire_nums = set(range(2 ** len(nums)))
        outputs = entire_nums.difference(nums_in_int)

        return bin(outputs.pop()).lstrip("0b").zfill(len(nums))


ans = Solution()
print(ans.findDifferentBinaryString(["1001", "1000", "0110", "1111"]))
