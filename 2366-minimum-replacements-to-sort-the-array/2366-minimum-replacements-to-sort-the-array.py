class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        

        right_min = nums[-1]
        answer = 0
        
        for i in range(len(nums)-1,-1,-1):
            
            if nums[i] > right_min:
                length = math.ceil(nums[i]/right_min)
                answer += length - 1
                right_min = math.floor(nums[i]/length )
            else:
                right_min = nums[i]
                
        
        return answer