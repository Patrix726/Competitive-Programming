# from itertools import combinations
# First solution didn't work

# class Solution:
#     def numOfSubarrays(self, arr: list[int]) -> int:
#         odds = list(filter(lambda num: num % 2 != 0, arr))
#         evens = list(filter(lambda num: num % 2 == 0, arr))
#         if len(odds) == 0:
#             return 0
#         oddComb = 0
#         for i in range(1, len(odds) + 1, 2):
#             oddComb += len(set(combinations(odds, i)))

#         evenComb = 0
#         for i in range(len(evens) // 2):
#             evenComb += len(set(combinations(evens, i))) * oddComb
#         return (oddComb + evenComb) % (10**9 + 7)

# def combination(self, n: int, r: int) -> int:
#     if n < r or n == 0:
#         return 0
#     return factorial(n) // (factorial(r) * factorial(n - r))


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        for i in range(n):
            arr[i] %= 2

        dpEven, dpOdd = [0] * n, [0] * n
        if arr[n - 1] == 0:
            dpEven[-1] = 1
        else:
            dpOdd[-1] = 1
        for i in range(n - 2, -1, -1):
            num = arr[i]
            if num == 0:
                dpEven[i] = (1 + dpEven[i + 1]) % MOD
                dpOdd[i] = dpOdd[i + 1]
            else:
                dpOdd[i] = (1 + dpEven[i + 1]) % MOD
                dpEven[i] = dpOdd[i + 1]
        count = 0
        for odd in dpOdd:
            count += odd
            count %= MOD
        return int(count)


ans = Solution()
print(ans.numOfSubarrays([100, 100, 99, 99]))
