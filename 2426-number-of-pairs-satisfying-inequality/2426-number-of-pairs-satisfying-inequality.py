class Solution:
    
    def merge_array(self,left_array,right_array):
        
        i = j = 0
        merged_array = []
        
        while i < len(left_array) and j < len(right_array):
            
            if left_array[i] <= right_array[j]:
                
                merged_array.append(left_array[i])
                i += 1
                
            else:
                
                merged_array.append(right_array[j])
                j+=1
        
        merged_array.extend(left_array[i:])
        merged_array.extend(right_array[j:])
        
        return merged_array
        
    
    
    def binary_search(self,num,nums,diff):
        
        left,right = 0,len(nums)
        
        while left < right:
            
            mid = (left + right)//2
            
            if num + diff < nums[mid]:
                right = mid 
            else:
                left = mid + 1
        
        return left 
    
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # equation is re-written as nums1[i] - nums2[i] - diff <= nums1[j]-nums2[j]
        # self.answer = 0
        def merge(left,right):
            
            if left == right:
                return [nums1[left]-nums2[left]],0
            
            mid = (left + right)//2
            left_array,l1 = merge(left,mid)
            right_array,l2= merge(mid+1,right)
            count = l1 + l2
            
            for num in right_array:
                
                count += self.binary_search(num,left_array,diff)
            
            return self.merge_array(left_array,right_array),count
        
        return merge(0,len(nums1)-1)[1]
            
            
        
        
            
            
        