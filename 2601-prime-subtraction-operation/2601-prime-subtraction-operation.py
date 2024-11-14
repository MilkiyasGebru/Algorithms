class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        # Implemnt sieve of erastohesis..
        
        prime = [False for _ in range(max(nums) + 1)]
        primes = []
        
        for i in range(2,len(prime)):
            
            if prime[i]:
                continue
                
            primes.append(i)
            inital = 2*i
            
            while inital < len(prime):
                
                prime[inital] = True
                inital += i
                
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i] < nums[i + 1]:
                continue
                
            for prime in primes:
                
                if nums[i] - prime < nums[i+1]:
                    nums[i] -= prime
                    break
                    
            if nums[i] <= 0 or nums[i] >= nums[i+1]:
                return False
            
        return True