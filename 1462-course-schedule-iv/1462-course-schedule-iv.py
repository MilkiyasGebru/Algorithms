class Solution:
    def addParent(self,node,parent,graph,ancestor):
        
        if parent in ancestor[node]:
            return 
        
        ancestor[node].add(parent)
        
        for child in graph[node]:
            self.addParent(child,parent,graph,ancestor)
            
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0  for _ in range(numCourses)]
        ancestor = defaultdict(set)
        graph = defaultdict(set)
        
        queue = deque()
        
        for pre,after in prerequisites:
            graph[pre].add(after)
            indegree[after]+=1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while(queue):
            parent = queue.popleft()
            for child in graph[parent]:
                self.addParent(child,parent,graph,ancestor)
                indegree[child]-=1
                if indegree[child]==0:
                    queue.append(child)
        answer = []
        for pre,after in queries:
            answer.append(pre in ancestor[after])
        return answer
        
        
        