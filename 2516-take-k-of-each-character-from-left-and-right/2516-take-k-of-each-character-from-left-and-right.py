class Solution:
    
    def isValid(self,s,length,k):
        total_freq = Counter(s)
        freq = Counter(s[:length])
        for i in range(length,len(s)):
            if total_freq['a'] - freq['a'] >= k and total_freq['b'] - freq['b'] >= k and total_freq['c'] - freq['c'] >= k:
                return True
            freq[s[i]] += 1
            freq[s[i-length]] -= 1
        return total_freq['a'] - freq['a'] >= k and total_freq['b'] - freq['b'] >= k and total_freq['c'] - freq['c'] >= k
            
    
    def takeCharacters(self, s: str, k: int) -> int:
        
        left = 0
        right = len(s) + 1
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.isValid(s,mid,k):
                left = mid + 1
            else:
                right = mid
        return len(s) - (left-1) if left-1 >=0 else -1
        
        