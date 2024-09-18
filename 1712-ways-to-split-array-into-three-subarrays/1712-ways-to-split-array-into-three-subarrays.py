class Solution:
    
    def binary_search(self,prefix,last_index):
        
        left = last_index + 1
        right = len(prefix) - 1
        
        while left < right:
            
            mid = (left + right)//2
            
            mid_sum = prefix[mid] - prefix[last_index]
            right_sum = prefix[-1] - prefix[mid]
            
            if  mid_sum <= right_sum:
                left = mid + 1
            else:
                right = mid
        return left-1
    def binary_search_II(self,prefix,last_index):
        
        left = last_index + 1
        right = len(prefix) - 1
        
        while left < right:
            mid = (left + right)//2
            
            left_sum = prefix[last_index]
            mid_sum = prefix[mid] - prefix[last_index]
            
            if mid_sum >= left_sum:
                right = mid
            else:
                left = mid + 1
        return  left
            
        
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        mod = 10**9 + 7
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        answer = 0
        for left in range(0,len(prefix)-2):
            answer +=  max(self.binary_search(prefix,left) - self.binary_search_II(prefix,left) + 1,0)
            answer %= mod
        return answer