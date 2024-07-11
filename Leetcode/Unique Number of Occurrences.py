def uniqueOccurrences(arr: list[int]) -> bool:
    a = set(arr)
    count = set()
    for i in a:
        leng = len(count)
        count.add(arr.count(i))
        if leng == len(count):
            return False
    return True


# def uniqueOccurrences(arr: list[int]) -> bool:
#     a = set(arr)
#     count = []
#     for i in a:
#         count.append(arr.count(i))
#     return len(set(count)) == len(count)


print(uniqueOccurrences([1, 2, 2]))
