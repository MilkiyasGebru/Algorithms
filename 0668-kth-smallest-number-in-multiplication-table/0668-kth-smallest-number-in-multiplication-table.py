class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        left = 1
        right = m*n
        
        def calculate(num):
            
            count = 0
            
            for i in range(m):
                
                count += min(n,num//(i+1))
            
            return count
        
        
        while(left <= right):
            
            mid = (left + right)//2
            count = calculate(mid)
            
            
            if count >= k:
                right = mid - 1
                
            else:
                left = mid + 1
                
       
        return left
            
            
            