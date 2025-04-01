
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        points = [0]*len(questions)

        for i in range(n-1,-1,-1):
            point, brain = questions[i]
            next = i + brain + 1
            if  next >= n:
                points[i] = max(point,points[i+1]) if i < n-1 else point
            else:
                points[i] = max(point + points[next],points[i+1])
        return max(points)
