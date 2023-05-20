class Solution:
    
    def calculate(self,node,end,visited,graph):
        
        if node in visited or graph[node] == [] or graph[end] == []:
            return -math.inf
        
        if node == end:
            return 1
        
        visited.add(node)
        val = -math.inf
        
        for child,wei in graph[node]:
            val = max(val, wei*self.calculate(child,end,visited,graph))
        return val
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
        
        answer = []
        for u,v in queries:
            answer.append(max(-1.0,self.calculate(u,v,set(),graph)))
        
        return answer
        
        