from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        output = []
        left = 0
        encounters = defaultdict(list)
        for i,char in enumerate(s):
            encounters[char].append(i)

        while left < len(s):
            l_char = s[left]
            last_encounter = encounters[l_char][-1]
            right = left + 1
            while right < last_encounter:
                r_char = s[right]
                last_encounter = max(last_encounter,encounters[r_char][-1])
                right+=1
            output.append(last_encounter-left+1)
            left = last_encounter+1
        return output

ans = Solution()
print(ans.partitionLabels('ababcc'))
