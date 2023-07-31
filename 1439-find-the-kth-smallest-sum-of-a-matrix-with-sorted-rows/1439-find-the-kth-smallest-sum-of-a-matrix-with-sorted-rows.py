class Solution:
    def isValid(self,col,n):
        return  0 <= col < n

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        inital_sum,arr = 0,[0 for _ in range(len(mat))]
        heap = []
        visited = set()
        for i in range(len(mat)):
            inital_sum += mat[i][0]
        
        heappush(heap,(inital_sum,arr))
        
        while k > 0:
            summ,arr = heappop(heap)
            
            if tuple(arr) in visited:
                continue
            visited.add(tuple(arr))
            k -= 1
            for i in range(len(arr)):
                if self.isValid(arr[i]+1,len(mat[0])):
                    new_arr = arr.copy()
                    new_arr[i] += 1
                    heappush(heap,(summ+mat[i][arr[i]+1]-mat[i][arr[i]],new_arr))
            
    
        return summ
            
        
        