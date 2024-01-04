class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        f = defaultdict(int)
        for num in nums:
            f[num] += 1
        min_operations = 0
        for key in f.keys():
            
            if f[key] == 1:
                return -1
            
            if f[key]%3 == 0:
                min_operations += f[key]//3
            elif f[key]%3 == 2:
                min_operations += (f[key]-2)//3 + 1
            else:
                min_operations += (f[key]-4)//3 + 2
        
        return min_operations
                