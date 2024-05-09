class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        diff = 0
        total = 0
        for i in range(k):
            total += max(happiness[i]-diff,0)
            diff += 1
        
        return total