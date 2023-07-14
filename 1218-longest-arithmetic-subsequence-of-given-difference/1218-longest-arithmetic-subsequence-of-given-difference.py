class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        maxLength = 0
        f = defaultdict(int)
        
        for i in range(len(arr)-1,-1,-1):
            
            f[arr[i]] = 1 + f[arr[i] + difference]
            maxLength = max(f[arr[i]], maxLength)
        
        return maxLength
        
        
        