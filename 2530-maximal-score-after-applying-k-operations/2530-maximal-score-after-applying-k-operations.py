class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        total = 0
        while(k>0):
            score = -1 * heapq.heappop(heap)
            total += score
            heapq.heappush(heap,-1*ceil(score/3))
            k-=1
        
        return total