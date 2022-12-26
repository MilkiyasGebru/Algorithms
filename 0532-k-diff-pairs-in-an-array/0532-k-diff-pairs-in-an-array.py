class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
       
        nums.sort()
        visited = set()
        answer = 0
        for left in range(len(nums)):
            right = left + 1
            
            while( right < len(nums) and nums[right] - nums[left] < k  ):
                right += 1
            
            if right < len(nums) and nums[right] not in visited and nums[right] - nums[left] == k:
                answer += 1
                visited.add(nums[right])
        
                
            
        return answer