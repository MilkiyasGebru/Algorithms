class Solution:
    def minDays(self, n: int) -> int:
        visited = set()
        heap = [(0,n)]
        while heap:
            
            days,num = heapq.heappop(heap)
            if num == 1:
                return days + 1
            if num in visited:
                continue
            visited.add(num)
            
            heapq.heappush(heap,(days + 1 + num%2,num//2))
            heapq.heappush(heap,(days + 1 + num%3,num//3))
        
            
            