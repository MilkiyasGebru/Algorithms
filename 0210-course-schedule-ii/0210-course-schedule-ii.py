class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        color = [0]*numCourses
        graph=defaultdict(list)
        
        for nextCourse,prevCourse in prerequisites:
            graph[prevCourse].append(nextCourse)
            
        ans = []
        def dfs(currentCourse):
            
            if color[currentCourse]==1:
                return True
            if color[currentCourse]==2:
                return False
            color[currentCourse]=1
            
            for nextCourse in graph[currentCourse]:
                if  dfs(nextCourse):
                    return True
            color[currentCourse]= 2
            ans.append(currentCourse)
        for i in range(numCourses):
            if dfs(i):
                return []
        return ans[::-1]
            
            
            
        