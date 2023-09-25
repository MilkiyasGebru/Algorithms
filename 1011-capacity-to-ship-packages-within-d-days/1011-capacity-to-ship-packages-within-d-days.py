class Solution:
    def count_days(self,weights,capacity):
        days = 0
        total_weight = 0
        for weight in weights:
            
            if total_weight + weight > capacity:
                days += 1
                total_weight =0 
            total_weight += weight
        
        return days if total_weight == 0 else days + 1
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left , right = max(weights),sum(weights) + 1
        
        while left < right:
            
            mid = ( left + right)//2
            if self.count_days(weights,mid) <= days:
                right = mid
            else:
                left = mid + 1
        
        return left