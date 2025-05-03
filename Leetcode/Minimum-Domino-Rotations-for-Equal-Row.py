from collections import Counter

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        top_count = Counter(tops)
        bottom_count = Counter(bottoms)
        top_common = top_count.most_common(1)[0]
        bottom_common = bottom_count.most_common(1)[0]
        if bottom_count[top_common[0]] < n - top_common[1] and top_count[bottom_common[0]] < n - bottom_common[1]:
            return -1
        top_rotations = 0
        is_top_valid = True
        bottom_rotations = 0
        is_bottom_valid = True
        for i in range(n):
            if tops[i] != top_common[0] and bottoms[i]==top_common[0]:
                top_rotations+=1
            elif tops[i] != top_common[0] and bottoms[i]!= top_common[0]:
                is_top_valid=False

            if bottoms[i] != bottom_common[0] and tops[i] == bottom_common[0]:
                bottom_rotations+=1
            elif bottoms[i] != bottom_common[0] and tops[i] != bottom_common[0]:
                is_bottom_valid = False
        if is_top_valid and is_bottom_valid:
            return min(top_rotations,bottom_rotations)
        elif is_top_valid:
            return top_rotations
        elif is_bottom_valid:
            return bottom_rotations
        return -1
