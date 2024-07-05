def increasingTriplet(nums: list[int]) -> bool:
    minimums = [[nums[0]]]
    for i in nums:
        for j in minimums:
            if i > j[-1]:
                j.append(i)
            elif i < j[-1] and i != j[0]:
                minimums.append([i])
                if i > j[0]:
                    j[-1] = i
                if len(j) == 1:
                    minimums.remove(j)
            if len(j) == 3:
                return True
    return False


print(increasingTriplet([2, 1, 5, 0, 4, 6]))
