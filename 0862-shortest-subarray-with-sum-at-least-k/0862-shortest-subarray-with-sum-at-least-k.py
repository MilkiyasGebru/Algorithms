class Solution:
    
    def add(self,q,num,i):
        while q and q[-1][0] >= num:
            q.pop()
            
        q.append((num,i))
        
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        q = deque([(0,-1)])
        total = size =  0
        answer = len(nums) + 1
        
        for i in range(len(nums)):
            
            total += nums[i]
                
            while q and total - q[0][0] >= k :
                
                node,index = q.popleft()
                answer = min(i - index ,answer)
            
            
            self.add(q,total,i)
        
        return answer if answer < len(nums)+1 else -1
            
            
            
            
            