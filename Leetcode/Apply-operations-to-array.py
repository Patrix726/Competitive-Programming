class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        output = []
        zeroCount = 0
        for i in range(len(nums)-1):
            num = nums[i]
            nextNum = nums[i+1]
            if num==0:
                zeroCount+=1
            elif num == nextNum:
                output.append(num*2)
                nums[i+1]=0
            else:
                output.append(num)
        if nums[-1]==0:
            zeroCount +=1
        else:
            output.append(nums[-1])
        output.extend([0]*zeroCount)
        return output