class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        self.parent = [-1] * n
        self.depth = [0]*n
        
        answer = []
        component_cost = [-1]*n

        for edge in edges:
            self._union(edge[0],edge[1])
        
        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]
        
        for start, end in query:
            st_root = self._find(start)
            en_root = self._find(end)
            if st_root == en_root:
                answer.append(component_cost[st_root])
            else:
                answer.append(-1)
        return answer

    def _find(self,node:int):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    def _union(self, node1:int, node2:int):
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 == root2:
            return
        
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1]+=1
