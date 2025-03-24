# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         meeting_days = set()
#         for start, end in meetings:
#             meeting_days.update(range(start,end+1))
#         return days - len(meeting_days)
        
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        print(meetings)
        right = 0
        meeting_count = 0
        for start, end in meetings:
            temp_right = max(start,right)
            if end >= temp_right:
                if temp_right ==start and temp_right != right:
                    meeting_count+=end-temp_right+1
                else:
                    meeting_count +=end-temp_right 
            right = max(temp_right,end)
        return days-meeting_count
        
