class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.total = 0
        
        def backTrack(index,arr):
            
            if index == len(nums):
                total_xor = 0
                for num in arr:
                    total_xor ^= num
                self.total += total_xor
                return
            
            backTrack(index+1,arr+[nums[index]])
            backTrack(index+1,arr)
        
        backTrack(0,[0])
        return self.total