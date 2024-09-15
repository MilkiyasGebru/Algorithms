class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        last_position = defaultdict(lambda : inf)
        freq = defaultdict(int)
        ans = 0
        last_position[(0,0,0,0,0)] =-1
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[s[i]] %= 2
            
            last_position[(freq["a"],freq["e"],freq["i"],freq["o"],freq["u"])] = min(
         last_position[(freq["a"],freq["e"],freq["i"],freq["o"],freq["u"])],
               i 
            )
            ans = max(ans, i -  last_position[(freq["a"],freq["e"],freq["i"],freq["o"],freq["u"])])
        return ans