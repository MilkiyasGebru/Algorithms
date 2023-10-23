class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(-math.inf)
        score = 0
        min_queue = deque()
        
        for i in range(k+1):
            
            index = math.inf
            while min_queue and min_queue[-1][0] > nums[i]:
                
                value,index = min_queue.pop()
            min_queue.append((nums[i],min(i,index)))
            
        for i in range(k+1,len(nums)):
            
            index = math.inf
            
            while min_queue and min_queue[-1][0] > nums[i]:
                
                value,index = min_queue.pop()
                if index <= k:
                    score = max(score, value*(i - index ))
                
            min_queue.append((nums[i],min(i,index)))
        return score
            