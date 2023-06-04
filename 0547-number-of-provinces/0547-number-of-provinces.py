class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent=[-1]*(len(isConnected)+1)
        rank=[0]*(len(isConnected)+1)
        def find(i):
            if parent[i]==-1:
                return i
            parent[i] = find(parent[i])
            
            return parent[i]
        def union(i,j):
            if rank[i] > rank[j]:
                parent[j]=i
            elif rank[j] > rank[i]:
                parent[i]=j
            else:
                rank[j]+=1
                parent[i]=j
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i==j or isConnected[i][j]==0:
                    continue
                p1=find(i)    
                p2 = find(j)
                if p1 == p2:
                    continue
                union(p1,p2)
        answer=-1
        for num in parent:
            if num==-1:
                answer+=1
        return answer        