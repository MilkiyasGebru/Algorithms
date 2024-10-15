class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ans = 0
        whitePosition = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += i - whitePosition
                whitePosition += 1
        return ans