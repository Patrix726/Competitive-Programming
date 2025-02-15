from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        sameAnswerCount = Counter(answers)
        unanswered = 0
        for answer, count in sameAnswerCount.items():
            remaining = count % (answer + 1)
            if remaining > 0:
                unanswered += answer + 1 - remaining
        return len(answers) + unanswered
