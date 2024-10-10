from collections import defaultdict


# Should have solved using stack
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        ans = [0 for i in range(length)]
        unans = defaultdict(list)
        for i in range(length):
            val = temperatures[i]
            for key in unans.keys():
                if val > key:
                    for x in unans[key]:
                        ans[x] = i - x
                    unans[key] = []
            unans[val].append(i)
        return ans


ans = Solution()
print(ans.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
