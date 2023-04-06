class Solution:
    def remove_all(self,q):
        while q:
            q.pop()
    
    def add(self,q,num,i):
        while q and q[-1][0] >= num:
            q.pop()
        q.append((num,i))
        
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        q = deque()
        total = size =  0
        answer = len(nums) + 1
        
        for i in range(len(nums)):
            
            total += nums[i]
            size += 1
            
            if total <= 0:
                self.remove_all(q)
                size = 0
                total = 0
                continue
            elif total >= k:
                answer = min(answer,size)
                
            while q and total - q[0][0] >= k :
                node,index = q.popleft()
                answer = min(i - index ,answer)
            
            
            self.add(q,total,i)
        
        return answer if answer < len(nums)+1 else -1
            
            
            
            
            