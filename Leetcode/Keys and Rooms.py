def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    d = dict(enumerate(rooms[1:], 1))
    accessKeys = rooms[0]
    while accessKeys:
        l = len(accessKeys)
        for i in range(l):
            ind = accessKeys.pop(0)
            item = d.pop(ind, None)
            if item:
                accessKeys += item
    return len(d) == 0


print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
