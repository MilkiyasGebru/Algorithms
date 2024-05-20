class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        new_array = [((nums[i]^k)-nums[i],nums[i]) for i in range(len(nums))]
        new_array.sort(reverse=True)
        
        i = total = 0
        
        while i+1 < len(new_array) and new_array[i][0] + new_array[i+1][0] >= 0: 
            
            total += new_array[i][0] + new_array[i+1][0] + new_array[i][1] + new_array[i+1][1]
            i += 2

        for j in range(i,len(new_array)):
            total += new_array[j][1]
        
        return total