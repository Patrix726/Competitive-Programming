def same_structure_as(arr1,arr2):
    both = isinstance(arr1,list) and isinstance(arr2,list)
    either = isinstance(arr1,list) or isinstance(arr2,list)
    if both:
        if len(arr1) != len(arr2):
            return False
        out = True
        for i in range(len(arr1)):
            out = out and same_structure_as(arr1[i],arr2[i])
        return out
    elif either:
        return False
    else:
        return True

arr1 = [1,[[],[]]]
arr2 = [2,[[2],[2]]]
print(same_structure_as(arr1,arr2))