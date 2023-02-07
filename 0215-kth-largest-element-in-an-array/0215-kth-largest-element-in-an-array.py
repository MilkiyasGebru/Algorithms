class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def find_pivot(left,right):
            pivot = left
            original_left = left
            p1 = left + 1
            left += 1
            while(left <= right):
                
                if nums[left] < nums[pivot]:
                    nums[left],nums[p1] = nums[p1],nums[left]
                    p1 += 1
                left += 1
            nums[pivot],nums[p1-1] = nums[p1-1],nums[pivot]
            pivot = p1 - 1
            
            if pivot == len(nums)-k:
                return pivot
            elif pivot > len(nums) - k:
                return find_pivot(original_left,pivot-1)
            else:
                return find_pivot(pivot + 1, right)
        
        return nums[find_pivot(0,len(nums)-1)]