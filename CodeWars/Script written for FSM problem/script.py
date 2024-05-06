eventDictionary = {}
with open("values.txt","r") as f:
    for line in f.readlines():
        splitLine = line.split(":")
        sec = splitLine[1].strip().split("->")
        state = splitLine[0].strip()
        event = sec[0].strip()
        finState = sec[1].strip()
        try: 
            if eventDictionary[state]:
                eventDictionary[state][event] = finState
            else:
                eventDictionary[state] = {event: finState}
        except:
            eventDictionary[state] = {event: finState}
        # try:
        #     if len(eventDictionary[state])>0:
        #         eventDictionary[state].append({event:finState})
        #     else:
        #         eventDictionary[state] = [{event:finState}]
        # except:
        #     eventDictionary[state] = [{event:finState}]
with open("output.txt","w") as f:
    f.write(str(eventDictionary))