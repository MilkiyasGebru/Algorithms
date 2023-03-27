class Solution:
    def merge_array(self,array1,array2):
        
        i = j = 0
        array = []
        
        while( i < len(array1) and j < len(array2)):
            
            if array1[i][0] <= array2[j][0]:
                array.append(array1[i])
                i+=1
                
            else:
                
                array.append(array2[j])
                j+=1
                
        array.extend(array1[i:])
        array.extend(array2[j:])
        
        return array
    
    def binary_search(self,num,nums):
        left,right = 0, len(nums)
        
        while left < right:
            
            mid = (left + right )//2
            
            if nums[mid][0] >= num:
                right = mid 
                
            else:
                left = mid + 1
                
        return left
        
            
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        answer =[0 for _ in range(len(nums))]
    
        def merge(left,right):
            
            if left == right:
                
                return [(nums[left],left)]
            
            mid = (left+right)//2
            
            left_array = merge(left,mid)
            right_array = merge(mid+1,right)
            
            for num,index in left_array:
                answer[index] += self.binary_search(num,right_array)
            
            return self.merge_array(left_array,right_array)
        
        merge(0,len(nums)-1)
        return answer
            
            