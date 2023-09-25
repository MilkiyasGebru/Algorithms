class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        left, right = 0,len(nums)
        
        while left < right:
            
            mid = (left + right) //2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        answer.append(left if (left < len(nums) and nums[left] == target) else -1)
        left,right = 0,len(nums)
        while left < right:
            
            mid = (left + right)//2
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        answer.append(left-1 if 0 <= left-1 < len(nums) and nums[left-1] == target else -1)
        return answer