class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        f = Counter(arr)
        g = Counter(f.values())
        
        return max(g.values()) == 1