import math


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip("-").isdecimal():
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                operation = self.operation(int(a), int(b), i)
                stack.append(operation)
        return stack.pop()

    def operation(self, a: int, b: int, operand: str):
        if operand == "+":
            return a + b
        elif operand == "-":
            return a - b
        elif operand == "*":
            return a * b
        else:
            val = a / b
            return math.floor(val) if val > 0 else math.ceil(val)


ans = Solution()
print(
    ans.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)
