class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        hashmap = {num: num for num in nums}
        changed = {}
        for key, val in operations:
            if key in changed:
                hashmap[changed[key]] = val
                changed[val] = changed[key]
            else:
                hashmap[key] = val
                changed[val] = key
        return [val for val in hashmap.values()]
