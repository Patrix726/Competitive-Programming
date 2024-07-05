def productExceptSelf(nums: list[int]) -> list[int]:
    product = 1
    numOfZeroes = 0
    for i in nums:
        if i == 0:
            numOfZeroes += 1
        else:
            product *= i
    if numOfZeroes == 0:
        return list(map(lambda x: product // x, nums))
    elif numOfZeroes == 1:
        return list(map(lambda x: 0 if x != 0 else product, nums))
    else:
        return list(map(lambda x: 0, nums))


print(productExceptSelf([-1, 1, -3, 3]))
