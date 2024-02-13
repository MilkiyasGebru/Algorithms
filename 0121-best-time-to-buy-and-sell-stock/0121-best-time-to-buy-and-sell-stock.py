class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = curr = 0
        inital = prices[0]
        
        for i in range(1,len(prices)):
            
            if prices[i] >= inital:
                profit = max(profit,prices[i] - inital)
            else:
                inital = prices[i]
        return profit