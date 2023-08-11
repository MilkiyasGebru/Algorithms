class Solution:
    def countBouqe(self,bloomDay,k,day):
        count = 0
        bouques = 0
        for i in range(len(bloomDay)):
            
            if day >= bloomDay[i]:
                count += 1
            else:
                count = 0
            if count == k:
                bouques += 1
                count =0 
        return bouques
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1
        
        left,right = 1,max(bloomDay) + 1
        
        while left < right:
            mid = (left + right)//2
            
            if self.countBouqe(bloomDay,k,mid) >= m:
                right = mid 
            else:
                left = mid + 1
        
        return left
        
        