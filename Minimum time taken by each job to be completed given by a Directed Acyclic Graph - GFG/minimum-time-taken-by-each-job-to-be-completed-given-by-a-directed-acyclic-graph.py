from typing import List


from typing import List
from collections import defaultdict,deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        
        graph = defaultdict(list)
        degree = [0 for _ in range(n)]
        answer = [0 for _ in range(n)]
        queue = deque()
        
        for u,v in edges:
            graph[u-1].append(v-1)
            degree[v-1] += 1
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)
        
        time = 1
        while queue:
            
            size = len(queue)
            for _ in range(size):
                
                node = queue.popleft()
                answer[node] = str(time)
                for child in graph[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        queue.append(child)
            
            time += 1
        return " ".join(answer)
                
            

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends