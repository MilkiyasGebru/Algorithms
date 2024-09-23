class Solution:
    
    def calculateNumber(self,prev,n):
        if prev == 0:
            return 0
        total = 0
        inital = 1
        while prev <= n :
            total += min(inital, max(n - prev + 1, 0))
            prev *= 10
            inital *= 10
        return total
    
    def findKthNumber(self, n: int, k: int) -> int:
        
        # Starting Number
        prev = 0
        another_count = 0
        while k > 0:
            another_count += 1
            for i in range(10):
                count = self.calculateNumber(prev*10 + i, n)
                if count < k:
                    k -= count
                else:
                    k -= 1
                    prev = 10*prev + i
                    break
        return prev
