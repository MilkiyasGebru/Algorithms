class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        total = 0
        for cost in costs:
            coins -= cost
            total += 1 if coins >= 0 else 0
        
        return total