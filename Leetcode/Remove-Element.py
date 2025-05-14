class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 1
        def findNext(index):
            while index <= len(nums):
                if nums[-index] == val:
                    index += 1
                else:
                    break
            return index
        index = findNext(index)
        i = 0
        while i <= len(nums)-index:
            if nums[i] == val:
                nums[-index],nums[i] = nums[i], nums[-index]
                index = findNext(index)
            
            i+=1
        return len(nums)-index + 1
