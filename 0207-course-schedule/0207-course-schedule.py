class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inDegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        courses = 0
        for ai,bi in prerequisites:
            graph[bi].append(ai)
            inDegree[ai] += 1
        
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
        
        while queue:
            
            size = len(queue)
            for _ in range(size):
                course = queue.popleft()
                courses += 1
                for ai in graph[course]:
                    inDegree[ai] -= 1
                    if inDegree[ai] == 0:
                        queue.append(ai)
        
        return courses == numCourses
        