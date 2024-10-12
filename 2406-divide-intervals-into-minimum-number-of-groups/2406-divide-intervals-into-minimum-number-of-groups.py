class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        heap = []
        answer = 0
        for i in range(len(intervals)):
            while heap and heap[0] < intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i][1])
            answer = max(answer,len(heap))
        return answer