class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        total = 0
        odd = 0
        f = Counter(s)
        for key in f.keys():
            
            if f[key] % 2 == 0:
                total += f[key]
            else:
                total += f[key] - 1
                odd = 1
        
        return total + odd