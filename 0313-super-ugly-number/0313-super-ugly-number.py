class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        visited = set()
        heap = [1]
        heapq.heappush(heap,1)
        last = 1
        while(n > 0):
            
            last = heapq.heappop(heap)
            if last in visited:
                continue
            visited.add(last)
            n-=1
            for prime in primes:
                heapq.heappush(heap,prime*last)
        return last