def predictPartyVictory(senate: str) -> str:
    queue = list(senate)
    ban = []
    i = 0

    while len(ban) != len(queue):
        if ban and ban[-1] == queue[i]:
            queue.pop(i)
            ban.pop()
            if i == len(queue):
                i = 0
        else:
            temp = "R" if queue[i] == "D" else "D"
            ban.append(temp)
            i = (i + 1) % len(queue)
    return "Radiant" if queue[0] == "R" else "Dire"


print(predictPartyVictory("RDD"))
