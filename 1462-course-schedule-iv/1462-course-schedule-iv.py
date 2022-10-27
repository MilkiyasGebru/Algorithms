class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dp=[[False for _ in range(numCourses)] for _ in range(numCourses)]
        
        for pre,after in prerequisites:
            dp[pre][after] = True
            
        for k in range(numCourses):
            
            for i in range(numCourses):
                
                for j in range(numCourses):
                    
                    dp[i][j] = dp[i][j] or  (dp[i][k] and dp[k][j])
                              
        return [dp[pre][after] for pre,after in queries]
                    