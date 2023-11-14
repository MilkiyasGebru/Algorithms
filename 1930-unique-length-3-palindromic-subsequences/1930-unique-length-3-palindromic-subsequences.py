class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        first = [len(s) for _ in range(26)]
        last = [-len(s) for _ in range(26)]
        
        for i in range(len(s)):
            
            val = ord(s[i])-ord('a')
            first[val] = min(first[val],i)
            last[val] = max(last[val],i)
            
        total_palindroms = 0
        
        for i in range(26):
            
            between = set()
            for j in range(first[i]+1,last[i]):
                between.add(s[j])
                
            total_palindroms += len(between)
        
        return total_palindroms