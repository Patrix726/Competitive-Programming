def parse_int(string:str):
    string=string.strip()
    if 'and' in string:
        if string.startswith('and'): string=string.removeprefix('and')
        if string.endswith('and') and not string.endswith('thousand'): string=string.removesuffix('and')
    string=string.strip()
    quantities = ['million','thousand','hundred']
    nums_in_string={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
                    'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
                    'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
                    'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,
                    'seventy':70,'eighty':80,'ninety':90 }
    nums =[]
    output=0
    if quantities[0] in string:
        nums = string.split(quantities[0])
        millions = nums[0]
        millions_in_num = parse_int(millions)
        output+=millions_in_num*1000000
        if (len(nums)>1) and nums[1]:
            output+=parse_int(nums[1])
        return output
    elif quantities[1] in string:
        nums = string.split(quantities[1])
        thousands = nums[0]
        thousands_in_num = parse_int(thousands)
        output+=thousands_in_num*1000
        if (len(nums)>1) and nums[1]:
            output+=parse_int(nums[1])
        return output
    elif quantities[2] in string:
        nums = string.split(quantities[2])
        hundreds = nums[0]
        hundreds_in_num = parse_int(hundreds)
        output+=hundreds_in_num*100
        # return parse_int(thousands)*1000 + parse_int(nums[1])
        if (len(nums)>1) and nums[1]:
            output+= parse_int(nums[1])
        return output
    elif 'ty' in string:
        nums = string.split('-')
        # tens = string.split('ty')[0]
        tens=nums[0]
        if (len(nums)>1) and nums[1]:
            return nums_in_string[tens] + parse_int(nums[1])
        return nums_in_string[tens]
    else:
        return nums_in_string[string]
print(parse_int("two thousand"))