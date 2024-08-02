from itertools import combinations


def combinationSum3(self, k: int, n: int) -> list[list[int]]:
    return list(filter(lambda x: sum(x) == n, combinations(range(1, 10), k)))


# class Solution:
#     def combinationSum3(self, k: int, n: int) -> list[list[int]]:
#         self.visited = set()
#         self.result = []
#         self.nums = range(1, n - 1)
#         self.length = k
#         self.expected = n
#         for i in range(1, 10):
#             self.backtrack(set(), 0, i)
#         return self.result

#     def backtrack(self, nums: set[int], sum: int, current: int):
#         nums.add(current)
#         self.visited.add(tuple(nums))
#         if sum + current == self.expected and len(nums) == self.length:
#             self.result.append(list(nums))
#             return
#         elif sum + current > self.expected or len(nums) == self.length:
#             return

#         for i in range(1, 10):
#             if i not in nums and tuple(nums.union([i])) not in self.visited:
#                 self.backtrack(nums.union([i]), sum + current, i)


# obj = Solution()

# print(obj.combinationSum3(3, 15))


# obj = Solution()
# print(obj.combinationSum3(3, 7))
