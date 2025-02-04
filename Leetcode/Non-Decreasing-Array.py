class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        stack = []
        index = 0

        while index < len(nums) - 1:
            if nums[index] > nums[index + 1]:
                if index > 0:
                    if nums[index + 1] >= nums[index - 1]:
                        stack.append(nums[index])
                    else:
                        stack.append(nums[index + 1])
                        nums[index + 1] = nums[index]
                else:
                    stack.append(nums[index])
            index += 1
        return len(stack) <= 1


# A better solution
# class Solution:
#     def checkPossibility(self, nums: List[int]) -> bool:
#         changed = False
#         for i in range(len(nums) - 1):
#             if nums[i] <= nums[i + 1]:
#                 continue
#             if changed:
#                 return False

#             if i == 0 or nums[i - 1] <= nums[i + 1]:
#                 nums[i] = nums[i + 1]
#             else:
#                 nums[i + 1] = nums[i]
#             changed = True
#         return True


ans = Solution()

print(ans.checkPossibility([2, 10, 3, 11]))
