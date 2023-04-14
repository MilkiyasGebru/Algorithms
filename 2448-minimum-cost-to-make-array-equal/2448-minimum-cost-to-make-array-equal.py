class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        prefix = defaultdict(int)
        
        for i in range(len(nums)):
            prefix[nums[i]] += cost[i]
            
        keys = sorted(prefix.keys())
        cost = 0
        
        for i in range(1,len(keys)):
            
            cost += (keys[i]-keys[0])*prefix[keys[i]]
            prefix[keys[i]] += prefix[keys[i-1]]
            
        answer = cost
        for i in range(1,len(keys)):
            
            cost = cost + (keys[i]-keys[i-1])*(2*prefix[keys[i-1]] - prefix[keys[-1]])
            answer = min(answer,cost)
        
        return answer
        