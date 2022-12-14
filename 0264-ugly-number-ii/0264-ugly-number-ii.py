class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = set()
        heap = [1]
        last = 1
        while(n > 0):
            
            last = heapq.heappop(heap)
            if last in visited:
                continue
            n-=1
            visited.add(last)
            for prime in [2,3,5]:
                heapq.heappush(heap,prime*last)
                
        return last