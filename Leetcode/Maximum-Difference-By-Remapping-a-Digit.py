class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        max_val = ""
        min_val = ""
        max_target = str_num[0]
        for char in str_num:
            if char != "9":
                max_target = char
                break
        min_target = str_num[0]
        for char in str_num:
            if char == max_target:
                max_val += "9"
            else:
                max_val += char
            if char == min_target:
                min_val += "0"
            else:
                min_val += char
        return int(max_val) - int(min_val)
        
