class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        arr = []
        
        for i in range(len(words[0])):
            
            f = defaultdict(int)
            
            for j in range(len(words)):
                f[words[j][i]] += 1
                
            arr.append(f)
            
        @lru_cache(None)
        def dp(arr_index,target_index):
            if target_index == len(target):
                return 1
            
            if arr_index == len(arr):
                return 0
            
            return arr[arr_index][target[target_index]]*dp(arr_index+1,target_index+1) + dp(arr_index+1,target_index)
        
        return dp(0,0)%(10**9+7)
