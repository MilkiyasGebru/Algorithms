class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_max = -math.inf
        current_min = maxx= nums[0]
        
        i = 0
        while i < len(nums):
            
            current_min,bit_length = nums[i],bin(nums[i]).count("1")
            
            while i < len(nums) and bit_length == bin(nums[i]).count("1") :
                
                maxx = max(nums[i],maxx)
                current_min = min(current_min,nums[i])
                i += 1
            if current_min < previous_max:
                return False
            
            previous_max = maxx
            
        return True
    