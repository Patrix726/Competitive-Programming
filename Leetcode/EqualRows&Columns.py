def equalPairs(grid: list[list[int]]) -> int:
    cols = {}
    for i in grid:
        for ind, val in enumerate(i):
            cols[ind] = cols.get(ind, []) + [val]
    count = 0
    columns = list(cols.values())
    for i in grid:
        count += columns.count(i)
    return count


print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
