class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        f = defaultdict(list)
        for i in range(len(nums)-1,-1,-1):
            max_arr = []
            
            for j in range(i+1,len(nums)):
                
                if nums[j] % nums[i] == 0 and len(max_arr) < len(f[nums[j]]):
                    max_arr = f[nums[j]]
            max_arr = max_arr.copy()
            max_arr.append(nums[i])
            f[nums[i]] = max_arr
        answer = []
        for key in f.keys():
            if len(f[key]) > len(answer):
                answer = f[key]
        
        return answer