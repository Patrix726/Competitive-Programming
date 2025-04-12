class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n - 1
        mid = (left+right)//2
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        mid = (left+right)//2
        left = 0
        right = m - 1
        idx = mid
        while left <= right:
            mid = (left+right)//2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] < target:
                left = mid+1
            else:
                right = mid -1
        return False
