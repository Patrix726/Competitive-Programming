
class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        total = 0
        for diff in differences:
            total+= diff
            min_val = min(min_val, total)
            max_val = max(max_val, total)
        max_min_diff = abs(max_val - min_val)
        available = upper - lower + 1
        if available - max_min_diff > 0:
            return available - max_min_diff
        else:
            return 0
