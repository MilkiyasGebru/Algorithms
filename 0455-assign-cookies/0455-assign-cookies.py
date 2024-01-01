class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        child = cookies = 0
        while child < len(g) and cookies < len(s):
            
            if s[cookies] >= g[child]:
                cookies += 1
                child += 1
            else:
                cookies += 1
        
        return child