from collections import deque


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    q = deque()
    q.append(entrance)

    m = len(maze[0])
    n = len(maze)
    moves = 0
    visited = {}
    while q:
        length = len(q)
        for i in range(length):
            pos = q.popleft()
            if (
                pos[0] == n - 1 or pos[1] == m - 1 or pos[0] == 0 or pos[1] == 0
            ) and pos != entrance:
                return moves

            below = [pos[0] + 1, pos[1]]
            beKey = "{0},{1}".format(str(below[0]), str(below[1]))
            above = [pos[0] - 1, pos[1]]
            abKey = "{0},{1}".format(str(above[0]), str(above[1]))
            left = [pos[0], pos[1] - 1]
            leKey = "{0},{1}".format(str(left[0]), str(left[1]))
            right = [pos[0], pos[1] + 1]
            riKey = "{0},{1}".format(str(right[0]), str(right[1]))

            if (
                below[0] != n
                and below != entrance
                and maze[below[0]][below[1]] != "+"
                and not visited.get(beKey, False)
            ):
                q.append(below)
                visited[beKey] = True

            if (
                above[0] != -1
                and above != entrance
                and maze[above[0]][above[1]] != "+"
                and not visited.get(abKey, False)
            ):
                q.append(above)
                visited[abKey] = True

            if (
                left[1] != -1
                and left != entrance
                and maze[left[0]][left[1]] != "+"
                and not visited.get(leKey, False)
            ):
                q.append(left)
                visited[leKey] = True

            if (
                right[1] != m
                and right != entrance
                and maze[right[0]][right[1]] != "+"
                and not visited.get(riKey, False)
            ):
                q.append(right)
                visited[riKey] = True

        moves += 1
    return -1


print(nearestExit([[".", "+"]], [0, 0]))
