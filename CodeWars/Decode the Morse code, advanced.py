def decode_bits(bits:str):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip("0")
    
    arr = bits.split("0")
    arr.sort()
    
    for i in arr:
        if i != '': 
           lenmin = len(i) 
           break
    lenmax = len(max(arr))
    mul = lenmin
    zeroes = arr.count('')
    if lenmin==lenmax and len(arr)>1:
        if zeroes<lenmin-1:
            mul=int(mul/3)
        else:
            if '' in arr or len(arr)==1:
                return bits.replace('0000000'*mul,'   ').replace('1'*mul,'.').replace('000'*mul, ' ').replace('0'*mul, '').replace('0','')
            return bits.replace('0000000','   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '').replace('0','')
    
    
    return bits.replace('0000000'*mul,'   ').replace('111'*mul, '-').replace('000'*mul, ' ').replace('1'*mul, '.').replace('0'*mul, '').replace('0','')

print(decode_bits('11111100111111'))