from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ind = 0
        players = list(range(1, n + 1))
        while len(players) > 1:
            ind = ind % len(players)
            ind = (ind + k - 1) % len(players)
            players.pop(ind)

        return players[0]


ans = Solution()
print(ans.findTheWinner(5, 2))
