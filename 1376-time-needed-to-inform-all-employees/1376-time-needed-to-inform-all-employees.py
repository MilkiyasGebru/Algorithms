class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = defaultdict(list)
        ans = 0
        for i in range(len(manager)):
            child[manager[i]].append(i)
        q=deque()
        q.append((headID,0))
        while q:
            
            node,time = q.popleft()
            ans = max(ans,time)
            
            for c in child[node]:
                q.append((c,time+informTime[node]))
        return ans
