class Solution:
    
    def merge_array(self,left_array,right_array):
        
        i = j = 0
        array = []
        while(i < len(left_array) and j < len(right_array)):
            
            if left_array[i] <= right_array[j]:
                array.append(left_array[i])
                i+=1
            else:
                array.append(right_array[j])
                j+=1
        array.extend(left_array[i:])
        array.extend(right_array[j:])
        return array
    
    def binary_search(self,num,nums):
        
        left,right = 0, len(nums)
        
        while left < right:
            
            mid = (left + right )//2
            
            if nums[mid] * 2 >= num:
                right = mid 
            else:
                left = mid + 1
                
        return left 
            
    
    def reversePairs(self, nums: List[int]) -> int:
        self.answer = 0
        
        def merge(left,right):
            
            if left == right:
                
                return [nums[left]]
            
            mid = (left + right )//2
            
            left_array = merge(left,mid)
            right_array = merge(mid+1,right)
            
            for num in left_array:
                self.answer += self.binary_search(num,right_array)
            
            return self.merge_array(left_array,right_array)
        
        merge(0,len(nums)-1)
        
        return self.answer 