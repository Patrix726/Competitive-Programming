mat = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
inp = input()
floor = int(input())


def indexOf(num):
    for i in mat:
        if num in i:
            return [mat.index(i), i.index(num)]


index = indexOf(floor)
for i in inp:
    if i == "U":
        index[0] -= 1
    elif i == "D":
        index[0] += 1
    elif i == "R":
        index[1] += 1
        index[1] %= 3
    else:
        index[0] -= 1
        index[1] %= 3
print(mat[index[0]][index[1]])
