class Solution:
    memo = {}
    def check(self,s):
        
        return s == s[::-1]
        
    def partition(self, s: str) -> List[List[str]]:
        
        answer = []
        if s in self.memo:
            return self.memo[s]
        for i in range(len(s)):
            
            if self.check(s[:i+1]):
                
                palindroms = self.partition(s[i+1:])
                
                if s == s[:i+1]:
                    answer.append([s])
                    
                for palindrom in palindroms:
                    answer.append([s[:i+1]] + palindrom)
            
        self.memo[s] = answer      
        return self.memo[s]
