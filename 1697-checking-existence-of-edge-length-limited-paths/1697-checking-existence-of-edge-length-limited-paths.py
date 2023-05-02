class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank =   [1 for _ in range(n)]
    
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionNode(self,node1,node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1 == parent2:
            return 
        if self.rank[parent2] > self.rank[parent1]:
            parent2,parent1=parent1,parent2
        
        self.rank[parent1] += self.rank[parent2]
        self.parent[parent2] = parent1
        return 

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = [False for _ in range(len(queries))]
        edgeList.sort(key = lambda x : x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key = lambda x : x[2])
        j = 0
        graph = UnionFind(n)
        
        for i in range(len(queries)):
            while j < len(edgeList) and edgeList[j][2] < queries[i][2]:
                graph.unionNode(edgeList[j][0],edgeList[j][1])
                j += 1
            answer[queries[i][-1]] = graph.findParent(queries[i][0]) == graph.findParent(queries[i][1])
        return answer
                
        