class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        sumofEven = 0
        answers = []
        for num in nums:
            if num % 2 == 0:
                sumofEven += num
        for query in queries:
            curNum = nums[query[1]]
            nums[query[1]] += query[0]

            wasEven = curNum % 2 == 0
            isEven = nums[query[1]] % 2 == 0
            if wasEven:
                sumofEven += query[0] if isEven else -1 * curNum
            elif isEven:
                sumofEven += nums[query[1]]
            answers.append(sumofEven)

        return answers


ans = Solution()
print(ans.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
