class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                break
        return i if coins < 0 else i + 1
            
        