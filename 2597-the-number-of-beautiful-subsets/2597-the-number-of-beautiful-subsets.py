class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        def backTrack(index,f):
            if index == len(nums):
                return 1
            
            total = backTrack(index+1,f)
            
            if f[nums[index]-k] == 0:
                f[nums[index]] += 1
                total += backTrack(index+1,f)
                f[nums[index]] -= 1
            return total
        
        return backTrack(0,defaultdict(int))-1