class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)
        
        dp =[[0 for _ in range(len(stones)+1)]for _ in range(len(stones)+1)]
        for left in range(len(stones),-1,-1):
            for right in range(len(stones)+1):
                if left >= right:
                    dp[left][right] = 0
                else:
                    dp[left][right] = max(
                     prefix[right]-prefix[left] - dp[left+1][right],
                        
                prefix[right-1] - prefix[left-1] - dp[left][right-1])

        
        return dp[1][-1]
    
            
            