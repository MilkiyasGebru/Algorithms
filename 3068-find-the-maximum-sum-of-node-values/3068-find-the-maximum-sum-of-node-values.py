class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        new_array = []
        for i in range(len(nums)):
            new_array.append(((nums[i]^k)-nums[i],nums[i]))
        new_array.sort(reverse=True)
        i = total = 0
        while i < len(new_array) and new_array[i][0] >= 0: 
            
            if i+1 < len(new_array) and new_array[i][0] + new_array[i+1][0] >= 0:
                total += new_array[i][0] + new_array[i+1][0] + new_array[i][1] + new_array[i+1][1]
            else:
                break
            i += 2
        
        for j in range(i,len(new_array)):
            total += new_array[j][1]
        
        return total