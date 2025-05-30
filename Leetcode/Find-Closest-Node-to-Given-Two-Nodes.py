class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        visited = {}
        curr1 = node1
        curr2 = node2 
        cost = 0
        while curr1 != -1:
            if curr1 in visited:
                break
            visited[curr1] = cost
            cost+=1
            curr1 = edges[curr1]

        min_cost = float('inf')
        found_node = None
        cost = 0
        cycle_check = set()
        while curr2 != -1:
            if curr2 in cycle_check:
                break
            if curr2 in visited:
                if max(cost, visited[curr2]) < min_cost:
                    min_cost = max(cost, visited[curr2])
                    found_node = curr2
                elif max(cost, visited[curr2]) == min_cost:
                    found_node = min(curr2,found_node) if found_node != None else curr2
            cycle_check.add(curr2)
            cost+=1
            curr2 = edges[curr2]
        return found_node if found_node != None else -1
