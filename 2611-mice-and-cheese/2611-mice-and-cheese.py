class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        heap = []
        total = 0
        for i in range(len(reward1)):
            total += reward1[i]
            heappush(heap,(reward1[i]-reward2[i]))
            
            if len(heap) > k:
                total -= heappop(heap)
        
        return total