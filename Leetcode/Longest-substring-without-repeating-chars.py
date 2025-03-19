class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = set()
        longest = 0
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right+=1
            else:
                longest = max(longest,right-left)
                while left <= right:
                    chars.discard(s[left])
                    if s[left] == s[right]:
                        left +=1
                        break
                    left +=1
        longest = max(longest,right-left)
        return longest
                    
