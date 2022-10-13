class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = defaultdict(list)
        
        for i in range(len(manager)):
            child[manager[i]].append(i)
        
        def dfs(node):
            if len(child[node]) == 0:
                return 0
            y = informTime[node] 
            x=-inf
            for c in child[node]:
                x = max(dfs(c),x)
            return x+y
        return dfs(headID)