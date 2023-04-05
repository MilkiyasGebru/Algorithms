class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
        right_array = [0 for _ in range(len(nums))]
        right_min = float("inf")
        
        left_max = nums[0]
        answer = 0
        
        for i in range(len(nums)-1,-1,-1):
            
            right_min = min(right_min,nums[i])
            right_array[i] = right_min
        
        for i in range(1,len(nums)-1):
            
            if left_max < nums[i] < right_array[i+1]:
                answer += 2
                
            elif nums[i-1] < nums[i] < nums[i+1]:
                answer += 1
                
            left_max = max(left_max,nums[i])
        
        return answer