class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = set(s)
        n = len(s)
        max_count = 0
        for char in alphabet:
            left = 0
            right = 0
            rem = k
            count = 0
            while right<n:
                if s[right]==char:
                    right+=1
                    count+=1
                elif rem > 0:
                    right+=1
                    count+=1
                    rem-=1
                else:
                    max_count = max(count,max_count)
                    while s[left]==char:
                        left+=1
                        count-=1
                    rem+=1
                    left+=1
                    count-=1
            max_count = max(count,max_count)
        return max_count
