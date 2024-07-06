def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    areas = []
    while l != r:
        area = min(height[l], height[r]) * (r - l)
        areas.append(area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max(areas)


print(maxArea([2, 3, 4, 5, 18, 17, 6]))
