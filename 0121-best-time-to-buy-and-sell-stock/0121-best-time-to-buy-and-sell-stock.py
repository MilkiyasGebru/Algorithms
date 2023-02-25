class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = prices[0]
        diff = 0
        for i in range(len(prices)):
            if first > prices[i]:
                first = prices[i]
            if prices[i]-first > diff:
                diff = prices[i]-first
        return diff       

    