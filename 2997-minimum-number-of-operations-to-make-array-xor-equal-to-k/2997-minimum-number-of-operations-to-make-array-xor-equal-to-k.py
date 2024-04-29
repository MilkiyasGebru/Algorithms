class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        arr = [0 for _ in range(24)]
        operations = 0

        for num in nums:
            
            for i in range(len(arr)):
                
                arr[i] += (1<<i)&(num) != 0
        for i in range(len(arr)):
            num = (1<<i) & (k) != 0
            odd = arr[i]%2 != 0
            
            add = (num & (not odd)) or ((not num) & (odd))
            operations += add
        
        return operations