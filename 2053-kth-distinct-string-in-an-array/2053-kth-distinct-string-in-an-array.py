class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        visited = set()
        f = Counter(arr)
        for element in arr:
            if f[element] == 1:
                k -= 1
            if k == 0:
                return element
        
        return ""