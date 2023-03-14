class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        graph = defaultdict(list)
        answer = [1 for i in range(n)]
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def rec(node):
            
            if node in visited:
                return ""
            visited.add(node)
            string = ""
            for neigbour in graph[node]:
                
                string += rec(neigbour)
            
            answer[node] += string.count(labels[node])
            
            return string+labels[node]
        
        rec(0)
        return answer
            
            
        
        