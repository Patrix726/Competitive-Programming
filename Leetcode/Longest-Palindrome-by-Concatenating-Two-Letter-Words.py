from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        palindromes = []
        pal_dict = defaultdict(int)
        center = 0

        for word in words:
            word_rev = "".join([word[1],word[0]])
            if word_rev in pal_dict:
                palindromes.append(pal_dict)
                pal_dict[word_rev] -= 1
                if pal_dict[word_rev] == 0:
                    del pal_dict[word_rev]
            else:
                pal_dict[word] += 1
        for word in pal_dict:
            if word[0] == word[1] and pal_dict[word]==1:
                center += 1
                break
        
        return len(palindromes) * 4 + center * 2
            
