class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[j] + nums[k]
                target = -1 * nums[i]
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return triplets


ans = Solution()
print(ans.threeSum([-1, 0, 1, 2, -1, -4]))
