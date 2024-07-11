def closeStrings(word1: str, word2: str) -> bool:
    a = set(word1)
    b = set(word2)
    if len(word1) != len(word2) or len(a) != len(b) or len(a.intersection(b)) != len(a):
        return False
    w1 = {}
    w2 = {}
    for i in range(len(word1)):
        w1[word1[i]] = w1.get(word1[i], 0) + 1
        w2[word2[i]] = w2.get(word2[i], 0) + 1
    operation1 = True
    switchedVals = [[], []]
    for k, v in w1.items():
        if v != w2[k]:
            operation1 = False
            if v in switchedVals[1]:
                switchedVals[1].remove(v)
            else:
                switchedVals[0].append(v)

            if w2[k] in switchedVals[0]:
                switchedVals[0].remove(w2[k])
            else:
                switchedVals[1].append(w2[k])
    return operation1 or (len(switchedVals[0]) == len(switchedVals[1]) == 0)


print(closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
