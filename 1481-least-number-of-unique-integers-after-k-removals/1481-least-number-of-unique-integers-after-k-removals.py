class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        f = list(Counter(arr).values())
        total = len(f)
        f.sort()
        
        for i in range(len(f)):
            
            if k - f[i] >= 0:
                total -= 1
                k -= f[i]
        
        return total
        