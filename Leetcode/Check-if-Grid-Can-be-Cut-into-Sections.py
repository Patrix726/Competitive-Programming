
class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x_intervals = []
        y_intervals = []

        for x1,y1,x2,y2 in rectangles:
            x_intervals.append([x1,x2])
            y_intervals.append([y1,y2])
        
        x_intervals.sort()
        y_intervals.sort()

        def check(intervals: list[list[int]]):
            output= [intervals[0]]
            for start, end in intervals[1:]:
                prev_end = output[-1][1]
                if start < prev_end:
                    output[-1][1] = max(prev_end,end)
                else:
                    output.append([start,end])
            return output
        x_count = len(check(x_intervals))
        y_count = len(check(y_intervals))
        return x_count >= 3 or y_count >= 3
