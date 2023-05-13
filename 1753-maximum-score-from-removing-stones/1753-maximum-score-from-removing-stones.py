class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        total_score = 0
        heap = []
        for i in [a,b,c]:
            if i > 0:
                heapq.heappush(heap,-i)
        
        while len(heap) > 1:
            
            total_score += 1
            one = heapq.heappop(heap)
            two = heapq.heappop(heap)
            
            if one + 1 < 0:
                heapq.heappush(heap,one+1)
            if two + 1 < 0:
                heapq.heappush(heap,two + 1)
        
        return total_score
            