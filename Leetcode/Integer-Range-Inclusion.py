class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        uncovered = set(range(left, right + 1))

        for intRange in ranges:
            covered = range(intRange[0], intRange[1] + 1)
            uncovered = uncovered.difference(covered)
        return len(uncovered) == 0
