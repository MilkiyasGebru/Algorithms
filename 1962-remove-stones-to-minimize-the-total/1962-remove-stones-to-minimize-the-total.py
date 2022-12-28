class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for pile in piles:
            heapq.heappush(heap,-1*pile)
            
        while(k>0):
            
            pile =-1* heapq.heappop(heap)
            pile = math.ceil(pile / 2)
            heapq.heappush(heap,-1*pile)
            k-=1
            
        total = 0
        
        for pile in heap:
            total += -1*pile
        
        return total