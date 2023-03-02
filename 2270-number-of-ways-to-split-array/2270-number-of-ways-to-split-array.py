class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total = sum(nums)
        summ =answer = 0
        for i in range(len(nums)-1):
            total -= nums[i]
            summ += nums[i]
            
            if summ >= total :
                answer += 1
        
        return answer