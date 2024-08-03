import heapq


def totalCost(costs: list[int], k: int, candidates: int) -> int:
    c = sorted([(x, i) for i, x in enumerate(costs)], key=lambda x: x[1])
    heapq.heapify(c)
    left = 0
    cost = 0
    for i in range(k):
        val = heapq.heappop(c)
        if val[1] >= left + candidates and val[1] <= len(c) - candidates + left:
            heapq.heappush(c, val)
        else:
            if val[1] < left + candidates:
                left += 1
            cost += val[0]

    return cost


print(totalCost([31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2))
