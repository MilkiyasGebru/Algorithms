class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        answer = time.copy()
        indegree = [0]*n
        graph=defaultdict(list)
        q=deque()
        for prevCourse, nextCourse in relations:
            indegree[nextCourse-1]+=1
            graph[prevCourse-1].append(nextCourse-1)
        
        for i in range(n):
            
            if indegree[i]==0:
                q.append(i)
                
        while(q):
            
            node = q.popleft()
            for child in graph[node]:
                answer[child]=max(time[child]+answer[node],answer[child])
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        return max(answer)