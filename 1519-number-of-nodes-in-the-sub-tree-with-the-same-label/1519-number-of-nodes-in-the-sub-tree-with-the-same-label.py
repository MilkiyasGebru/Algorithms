class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        graph = defaultdict(list)
        answer = [1 for i in range(n)]
        visited = set()
        
        for u,v in edges:
            
            graph[u].append(v)
            graph[v].append(u)
        
        def rec(node):
            
            string = Counter()
            
            if node not in visited:
                
                visited.add(node)

                string[labels[node]] = 1
                for neigbour in graph[node]:

                    string += rec(neigbour)

                answer[node] = string[labels[node]]
            
            return string
        
        rec(0)
        return answer
            
            
        
        