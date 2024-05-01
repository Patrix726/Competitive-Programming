""" 
Greed is a dice game played with five six-sided dice. 
Your mission, should you choose to accept it, is to score 
a throw according to these rules. you will be given an array 
with five six-sided dice values.
    Three 1's = 1000
    Three 6's = 600
    Three 5's = 500
    Three 4's = 400
    Three 3's = 300
    Three 2's = 200
    One 1 = 100
    One 5 = 50
Note: A single die can only be counted once in each roll.
 """
def score(arr:list):
    values = [1,2,3,4,5,6]
    outputScore=0
    if (len(arr)==0): return
    elif len(arr)>=3:
        for i in values:
            count = arr.count(i)
            if count >=3:
                if i ==1: outputScore+=int(count/3) * 1000 
                else: outputScore+=int(count/3) * i*100
                if count%3!=0:
                    if i==1: outputScore+=(count%3)*100
                    elif i==5: outputScore+= (count%3)*50
                # return outputScore+score(arr)
            else:
                if i==1: outputScore+=count*100
                elif i==5: outputScore+= count*50
    return outputScore

            
