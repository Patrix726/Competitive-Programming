import math


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        horizontal = {}
        vertical = {}
        cube = {}
        horizontalNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        verticalNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cubeNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if not num.isdigit():
                    continue
                curHor: set = horizontal.get(i, set())
                curHor.add(num)
                horizontal[i] = curHor
                horizontalNums[i] += 1
                if len(curHor) != horizontalNums[i]:
                    return False

                curVer: set = vertical.get(j, set())
                curVer.add(num)
                vertical[j] = curVer
                verticalNums[j] += 1
                if len(curVer) != verticalNums[j]:
                    return False
                cubeInd = 3 * math.floor(i / 3) + math.floor(j / 3)
                curCube: set = cube.get(cubeInd, set())
                curCube.add(num)
                cube[cubeInd] = curCube
                cubeNums[cubeInd] += 1
                if len(curCube) != cubeNums[cubeInd]:
                    return False
        return True


ans = Solution()
print(
    ans.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
