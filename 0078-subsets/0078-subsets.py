class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        total_arr = []
        def backTrack(index,arr,total_arr):
            if index == len(nums):
                total_arr.append(arr.copy())
                return
            
            backTrack(index+1,arr+[nums[index]],total_arr)
            backTrack(index+1,arr,total_arr)
        
        backTrack(0,[],total_arr)
        return total_arr
            