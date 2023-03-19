class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        cookies.sort(reverse = True)
        self.max = math.inf
        arr = [0 for _ in range(k)]
        
        def backtrack(i):
            
            if i == len(cookies):
                
                self.max = min(self.max,max(arr))
                return
            
            for j in range(k):
                
                if arr[j] + cookies[i] < self.max:
                    
                    arr[j] += cookies[i]
                    backtrack(i+1)
                    arr[j] -= cookies[i]
                    
        
        backtrack(0)
        return self.max
            