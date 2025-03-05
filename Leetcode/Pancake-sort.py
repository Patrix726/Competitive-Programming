class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        sorted_arr = list(sorted(arr))
        if arr == sorted_arr:
            return []
        output = []

        def recurse(nums: list[int], end: int):
            if nums == sorted_arr or end == 0:
                return
            max_num = max(nums[0:end])
            max_index = nums.index(max_num)

            while max_index != end - 1 and max_index != 0:
                k = max_index + 1
                nums = (
                    list(reversed(nums[:k])) + nums[k:]
                    if k < len(nums)
                    else list(reversed(nums[:k]))
                )
                max_index = 0
                output.append(k)
            if max_index != end - 1:
                k = end
                nums = (
                    list(reversed(nums[:k])) + nums[k:]
                    if k < len(nums)
                    else list(reversed(nums[:k]))
                )
                output.append(k)
            end -= 1
            recurse(nums, end)

        recurse(arr, len(arr))
        return output
