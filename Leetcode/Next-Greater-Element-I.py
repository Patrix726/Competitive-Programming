
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        elements = {}
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            elements[num] = stack[-1] if stack else -1
            stack.append(num)
        output = []
        for num in nums1:
            output.append(elements[num])
        return output
        



