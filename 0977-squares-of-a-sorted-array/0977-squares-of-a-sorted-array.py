class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        postive = len(nums)
        negative = -1 
        
        for i in range(len(nums)):
            
            if nums[i] < 0:
                
                negative = max(negative, i)
                
            else:
                
                postive = min(postive, i)
        
                
        while(negative > -1 or postive < len(nums)):
            if negative == -1 or( postive < len(nums) and nums[postive] < abs(nums[negative])):
                
                answer.append(nums[postive]*nums[postive])
                postive += 1
                
            else:
                
                answer.append(nums[negative]*nums[negative])
                negative -= 1
            
        
        return answer