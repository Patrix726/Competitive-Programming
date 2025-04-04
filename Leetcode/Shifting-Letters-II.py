
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        prefix = [0]*n
        for start, end, dir in shifts:
            prefix[start]+=-1 if dir==0 else dir
            if end + 1 < n:
                prefix[end+1] -= -1 if dir == 0 else dir
        cur_shift = 0
        output = ""
        for char,shift in zip(s,prefix):
            cur_shift+=shift
            output+=self.shiftLetter(char,cur_shift)
        return output
    def shiftLetter(self,char:str,amt:int):
        base = 97
        val = ord(char)
        chgd = (val + amt - base)%26
        return chr(base + chgd)

