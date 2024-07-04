def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
        else:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
    return n <= 0


print(canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1))
