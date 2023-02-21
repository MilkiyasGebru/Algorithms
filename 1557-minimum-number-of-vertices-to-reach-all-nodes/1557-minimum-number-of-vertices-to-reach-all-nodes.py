class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree=[0]*(n)
        
        for v1,v2 in edges:
            degree[v2]+=1
        answer=[]
        for i in range(len(degree)):
            if degree[i]==0:
                answer.append(i)
        return answer        