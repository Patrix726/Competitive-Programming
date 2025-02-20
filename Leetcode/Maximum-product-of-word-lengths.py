class Solution:
    def maxProduct(self, words: list[str]) -> int:
        max_product = 0
        for f_word in words:
            f_set = set(f_word)
            for s_word in words:
                if f_set.isdisjoint(s_word):
                    max_product = max(max_product, len(f_word) * len(s_word))
        return max_product
