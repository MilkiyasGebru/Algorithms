class Solution:

    def __init__(self, nums: List[int]):
        
        self.f = defaultdict(list)
        
        for i in range(len(nums)):
            
            self.f[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        
        return self.f[target][randint(0,len(self.f[target])-1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)