class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        colors = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        
        for course1,course2 in prerequisites:
            graph[course2].append(course1)
        
        def dfs(course):
            
            colors[course] = 1
            answer = True
            
            for neigbour in graph[course]:
                
                if colors[neigbour] == 0:
                    answer = answer and dfs(neigbour)
                    
                elif colors[neigbour] == 1:
                    answer = False
                    break
                    
            colors[course] = 2
            
            return answer
        
        answer = True
        
        for course in range(numCourses):
            
            answer = answer and dfs(course)
        
        return answer
                
                
            
            