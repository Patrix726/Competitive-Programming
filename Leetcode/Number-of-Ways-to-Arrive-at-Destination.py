import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 1_000_000_007
        edges = [[] for _ in range(n)]

        for u,v,cost in roads:
            edges[u].append((v,cost))
            edges[v].append((u,cost))
        shortestTime = [float('inf')]*n
        pathCount = [0]*n

        shortestTime[0] = 0
        pathCount[0] = 1
        min_heap = [(0,0)]
        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if cost > shortestTime[node]:
                continue
            
            for neighbor, time in edges[node]:
                if cost + time < shortestTime[neighbor]:
                    shortestTime[neighbor] = cost + time
                    pathCount[neighbor] = pathCount[node]
                    heapq.heappush(min_heap, (shortestTime[neighbor], neighbor))
                elif cost + time == shortestTime[neighbor]:
                    pathCount[neighbor] = (pathCount[neighbor] + pathCount[node]) % MOD
        return pathCount[n-1]
