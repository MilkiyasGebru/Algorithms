class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        colors = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        
        for course1,course2 in prerequisites:
            graph[course2].append(course1)
        
        answer = []
        
        
        def dfs(course):
            
            colors[course] = 1
            
            for neigbour in graph[course]:
                
                if colors[neigbour] == 0:
                    dfs(neigbour)
                elif colors[neigbour] == 1:
                    return
            
            colors[course] = 2
            answer.append(course)
        
        for course in range(numCourses):
            if colors[course] == 0:
                dfs(course)
        return answer[::-1] if len(answer) == numCourses else []