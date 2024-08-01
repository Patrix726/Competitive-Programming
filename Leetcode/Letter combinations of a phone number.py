class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.result = []
        self.visited = set()
        dig_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if not digits:
            return []
        self.backtrack([dig_letter[x] for x in digits], "", -1)
        return self.result

    def backtrack(self, paths: list, path: str, current: int):
        if current == len(paths) - 1:
            self.result.append(path)
            return
        self.visited.add(path)
        next_path = paths[current + 1]
        for i in range(len(paths[current + 1])):
            new_path = path + next_path[i]
            if new_path not in self.visited:
                self.backtrack(paths, new_path, current + 1)


obj = Solution()
print(obj.letterCombinations("23"))
