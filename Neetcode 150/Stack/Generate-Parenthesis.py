class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.solutions = []
        self.limit = 2 * n
        self.recursiveParenthesis("", n, n)
        return self.solutions

    def recursiveParenthesis(self, s: str, lb: int, rb: int):
        if lb == 0 and len(s) == self.limit:
            self.solutions.append(s)
            return

        for i in ["(", ")"]:
            if rb == 0:
                return
            if i == ")" and lb < rb:
                self.recursiveParenthesis(s + i, lb, rb - 1)
            if i == "(" and lb != 0:
                self.recursiveParenthesis(s + i, lb - 1, rb)


ans = Solution()
print(ans.generateParenthesis(1))
