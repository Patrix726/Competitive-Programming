class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat_count = 0
        people.sort()
        left = 0
        right = len(people)-1
        while left <= right:
            if people[left]+people[right] > limit:
                right-=1
            else:
                left+=1
                right-=1
            boat_count+=1
        return boat_count

