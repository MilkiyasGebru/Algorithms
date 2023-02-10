class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                if nums[i] + nums[j] == target:
                    answer += 1
                if nums[j] + nums[i] == target:
                    answer += 1
        return answer 