class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                answer += 1
        
        return answer if  nums[0] == 0 else answer + 1