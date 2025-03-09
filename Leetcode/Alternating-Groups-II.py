
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        colors += colors[:k]
        switch = 1
        count = 0
        for i in range(1,len(colors)):
            if switch == k:
                count+=1
                switch-=1
            if colors[i]==colors[i-1]:
                switch = 1
            else:
                switch+=1
        return count

ans = Solution()
print(ans.numberOfAlternatingGroups([0,1,0,1,0],3))
