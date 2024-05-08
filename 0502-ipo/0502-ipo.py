class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        array = [(profits[i],capital[i]) for i in range(len(profits))]
        array.sort(key = lambda x : x[1])
        i = 0
        
        heap = []
        while k :
            while i < len(array) and array[i][1] <= w:
                
                heapq.heappush(heap,-array[i][0])
                i += 1
            
            if not heap:
                break
            value = heapq.heappop(heap)
            w += -1*value
            k -= 1
            
        return w 
            
            