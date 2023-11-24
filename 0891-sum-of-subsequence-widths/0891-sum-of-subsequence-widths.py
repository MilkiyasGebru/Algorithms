class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        
        nums.sort()
        mod = 10**9 + 7
        answer = 0
        for i in range(len(nums)-1,-1,-1):
            
            max_num = pow(2,i,mod)
            min_num = pow(2,len(nums)-1-i,mod)
            answer += nums[i]*(max_num - min_num)
            answer %= mod
        
        return answer
            