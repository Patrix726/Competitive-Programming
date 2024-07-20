from collections import deque


def findCircleNum(isConnected: list[list[int]]) -> int:
    nodes = dict(enumerate(isConnected))
    provinces = []
    while nodes:
        pr = findProvinces(nodes, list(nodes.keys())[0], set())
        for ind in pr:
            nodes.pop(ind)
        provinces.append(pr)

    return len(provinces)


def findProvinces(nodes: dict[list[int]], index: int, previous: set[int]):
    if len(previous) == len(nodes):
        return set([index])
    node = set([ind for ind, val in enumerate(nodes.get(index)) if val == 1])
    node = node.difference(previous)
    if len(node) < 1:
        return set([index])
    else:
        for x in node:
            if x != index:
                node = node.union(findProvinces(nodes, x, node.union(previous)))

        return node


print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
