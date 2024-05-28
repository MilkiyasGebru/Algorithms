class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        left = ans = 0
        for right in range(len(s)):
            
            maxCost -= abs(ord(s[right])-ord(t[right]))
            while maxCost < 0:
                maxCost += abs(ord(s[left])-ord(t[left]))
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
            