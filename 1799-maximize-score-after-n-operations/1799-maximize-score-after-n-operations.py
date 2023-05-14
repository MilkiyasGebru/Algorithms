class Solution:
    
    @lru_cache(None)
    def cal_gcd(self,num1,num2):
        if num2 == 0:
            return num1
        return self.cal_gcd(num2,num1%num2)
    
    def maxScore(self, nums: List[int]) -> int:
        
        arr = [ ]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num = self.cal_gcd(nums[j],nums[i])
                bit_mask = (1 << i) ^ (1 << j)
                arr.append((num,bit_mask))
        arr.sort()
        
        @lru_cache(None)
        def dp(i,mask,count):
            if i == len(arr) or count == len(nums)//2 + 1:
                return 0
            
            if not (mask & arr[i][1]):
                
                return max(count*arr[i][0] + dp(i+1,mask^arr[i][1],count+1),dp(i+1,mask,count))
            
            return dp(i+1,mask,count)
        
        return dp(0,0,1)
        
            
                            
            