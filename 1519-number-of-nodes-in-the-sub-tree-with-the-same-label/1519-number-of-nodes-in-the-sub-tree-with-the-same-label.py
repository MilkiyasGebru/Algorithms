class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        graph = defaultdict(list)
        answer = [0 for i in range(n)]
        # visited = set()
        
        for u,v in edges:
            
            graph[u].append(v)
            graph[v].append(u)
        
        def rec(child,parent,count):
            
            before = count[labels[child]]
            count[labels[child]] += 1
            
            for neigbour in graph[child]:
                if neigbour != parent:
                    rec(neigbour,child,count)
            
            answer[child] = count[labels[child]] - before
        
        rec(0,0,defaultdict(int))
        return answer
            
            
        
        