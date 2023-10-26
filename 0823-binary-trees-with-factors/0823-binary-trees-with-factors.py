class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        mod = 10**9 + 7
        f = defaultdict(int)
        for ele in arr:
            f[ele] += 1
        
        arr.sort()
        for i in range(1,len(arr)):
            
            for left in range(i):
                
                f[arr[i]] += f[arr[left]]*f[arr[i]/arr[left]]
        
                f[arr[i]] %= mod
        
        return sum(f.values())%mod