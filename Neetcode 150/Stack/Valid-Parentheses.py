class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = ["(", "{", "["]
        closeBrackets = [")", "}", "]"]
        for i in s:
            if i in openBrackets:
                stack.append(i)
            else:
                if len(stack) == 0 or openBrackets.index(
                    stack[-1]
                ) != closeBrackets.index(i):
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
