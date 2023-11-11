class Solution:
    def countHomogenous(self, s: str) -> int:
        
        left = ans = 0
        for right in range(len(s)):
            
            while s[left] != s[right]:
                left += 1
            
            ans += right - left + 1
        
        return ans%(10**9 + 7)