class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        n = len(blocks)
        if k == n:
            return blocks.count("W")
        count = 0
        min_count = 101
        while right < n:
            if blocks[right] == "W":
                count += 1
            if right - left == k - 1:
                min_count = min(min_count, count)
            elif right - left > k - 1:
                if blocks[left] == "W":
                    count -= 1
                left += 1
                min_count = min(min_count, count)
            right += 1

        return min_count


ans = Solution()
print(
    ans.minimumRecolors(
        "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW", 29
    )
)
