class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        self.d = {}
        for i in range(len(equations)):
            a, b = equations[i]
            vala = self.d.get(a, [])
            valb = self.d.get(b, [])
            vala.append((b, values[i]))
            valb.append((a, 1 / values[i]))
            self.d[a] = vala
            self.d[b] = valb
        output = []
        for a, b in queries:
            if self.d.get(a, None) and self.d.get(b, None):
                if a == b:
                    output.append(1.0)
                else:
                    added = False
                    for node in self.d.get(a, []):
                        if node[0] == b:
                            output.append(node[1])
                            added = True
                            break

                        res = self.dfs(node, [a], b)
                        if res:
                            added = True
                            output.append(res * node[1])
                            break
                    if not added:
                        output.append(-1.0)
            else:
                output.append(-1.0)
        return output

    def dfs(self, node: tuple, parent: list[str], target: str):
        k, v = node
        for a, b in self.d.get(k, []):
            if a in parent:
                continue
            if a == target:
                return b
            val = self.dfs((a, b), parent + [k], target)
            if val:
                return b * val

        return None


print(
    Solution().calcEquation(
        [["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]],
        [3.0, 0.5, 3.4, 5.6],
        [
            ["x2", "x4"],
            ["x1", "x5"],
            ["x1", "x3"],
            ["x5", "x5"],
            ["x5", "x1"],
            ["x3", "x4"],
            ["x4", "x3"],
            ["x6", "x6"],
            ["x0", "x0"],
        ],
    )
)
