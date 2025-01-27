class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                result += i.lower()
        print(result)
        return result == result[::-1]


ans = Solution()
print(ans.isPalindrome("0P"))
