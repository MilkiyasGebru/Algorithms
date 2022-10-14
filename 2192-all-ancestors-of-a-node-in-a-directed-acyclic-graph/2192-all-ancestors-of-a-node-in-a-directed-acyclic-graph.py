class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph= defaultdict(list)
        answer = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
        
        def dfs(node,parent):
            
            if answer[node] and answer[node][-1]==parent:
                return
            if node != parent:
                answer[node].append(parent)
            
            for child in graph[node]:
                dfs(child,parent)
            
        for v in range(n):
            dfs(v,v)
        return answer