class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        output = [words[0]]
        target = 1 - groups[0]

        for word, group in zip(words,groups):
            if target == group:
                output.append(word)
                target = 1 - group
        return output
