class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        left = coins = 0
        right = len(piles)-2
        
        while left < right:
            coins += piles[right]
            left += 1
            right -= 2
        
        return coins