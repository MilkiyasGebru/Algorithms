class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        answer = []
        
        i = 0
        while i < len(nums):
            
            if nums[i+2] - nums[i] <= k:
                answer.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
            
            i += 3
        
        return answer
            