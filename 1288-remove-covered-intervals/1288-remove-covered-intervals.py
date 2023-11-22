class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : (x[0],-x[1]))
        stack = []
        
        for i in range(len(intervals)-1,-1,-1):
            u,v = intervals[i]
            while stack and stack[-1][0] >= u and stack[-1][1] <= v:
                stack.pop()
            stack.append((u,v))
        return len(stack)