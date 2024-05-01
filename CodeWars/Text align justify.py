def justify(text:str, width:int):
    text=text.strip()
    words = text.split()
    curLine = 0
    curWords = []
    output=""
    for i in range(len(words)):
        curLine+=len(words[i])+1
        if curLine-1 <= width:
            curWords.append(words[i])
        else:
            output+=formLine(curWords,width).strip()+"\n"
            curLine=len(words[i])+1
            curWords = [words[i]]
    if curWords:
        output+=" ".join(curWords)
    return output
def formLine(words:list, width:int):
    joined = "".join(words)
    if len(words)<=1:
        return joined
    allgap = width-len(joined)
    gap = allgap/(len(words)-1)
    remainder=allgap-(gap*len(words)-1)
    remainder+=gap
    if round(gap)>=gap:
        gap=int(round(gap))
        remainder=allgap%gap
    else:
        gap=int(round(gap))
        remainder=allgap-(gap*len(words)-1)
        remainder+=gap
    output=""
    for i in range(len(words)):
        if remainder>gap:
            if i==0:
                output+=words[i] + " "*remainder
            else:
                output+=words[i] + " "* gap
        else:
            if i==(len(words)-2) and remainder:
                output+=words[i] + " "* remainder
            else:
                output+=words[i] + " "* gap
    return output
print(justify("zDsxhlt vm leVDGnOHf DU aAIUKFIY ipuMmDdCZt XbZ fqpMTEWVM eWjmlDO K VCZoz HUmemMxt ZYHMGlrCg zaJaiF qYQgivBy clbmBItgA evuYDmzIat WfTeube f DOzsvG a j cOp bJMNA WUzxS mz" , 46))
