class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = lambda x : x[1])
        ans = 0
        last = -math.inf
        
        for i in range(len(pairs)):
            if pairs[i][0] > last:
                last = pairs[i][1]
                ans += 1
        
        
        
        return ans
            