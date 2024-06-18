class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        array = [(difficulty[i],profit[i]) for i in range(len(profit))]
        array.sort()
        worker.sort()
        total = 0
        max_profit = 0
        i = 0
        j = 0
        while i < len(worker):
            
            while j < len(array) and array[j][0] <= worker[i]:
                
                max_profit = max(array[j][1], max_profit)
                j += 1
                
            i += 1
            total += max_profit
        
        return total
                