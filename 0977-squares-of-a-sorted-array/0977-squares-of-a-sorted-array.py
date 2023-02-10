class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        left = 0
        right = len(nums)-1
        
        while(left <= right):
            
            if abs(nums[left]) > abs(nums[right]):
                answer.append(nums[left] * nums[left])
                left += 1
            else:
                answer.append(nums[right] * nums[right])
                right -= 1
        
        answer.reverse()
        return answer