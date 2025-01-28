class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        maxVolume = -1
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            maxVolume = max(volume, maxVolume)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxVolume


ans = Solution()

print(ans.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
