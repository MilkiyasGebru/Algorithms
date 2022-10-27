class Solution:
    def addParent(self,node,par,graph,parent):
        
        if par in parent[node]:
            return 
        
        parent[node].add(par)
        
        for child in graph[node]:
            self.addParent(child,par,graph,parent)
            
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0  for _ in range(numCourses)]
        parent = defaultdict(set)
        graph = defaultdict(set)
        
        queue = deque()
        
        for pre,after in prerequisites:
            graph[pre].add(after)
            indegree[after]+=1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while(queue):
            node = queue.popleft()
            for child in graph[node]:
                self.addParent(child,node,graph,parent)
                indegree[child]-=1
                if indegree[child]==0:
                    queue.append(child)
        answer = []
        for pre,after in queries:
            answer.append(pre in parent[after])
        return answer
        
        
        