class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        total = []
        def backTrack(i,arr,answer):
            
            if i == len(nums):
                answer.append(arr.copy())
                return
            
            for num in nums:
                if num not in arr:
                    backTrack(i+1,arr+[num],answer)
            
        
        backTrack(0,[],total)
        return total