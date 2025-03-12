class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        teamSkill = sum(skill)/(len(skill)/2)
        left = 0
        right = len(skill)-1
        totalChem = 0
        while left < right:
            if skill[left] + skill[right] != teamSkill:
                return -1
            totalChem += skill[left] * skill[right]
            left +=1
            right-=1
        return totalChem
