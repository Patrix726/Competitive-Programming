class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()

        n = len(processorTime)
        maxTime = 0

        for i in range(n):
            cur_processor = processorTime[i]
            cur_time = max([cur_processor + task for task in tasks[4*i:4*(i+1)]])
            maxTime = max(maxTime,cur_time )
        return maxTime
