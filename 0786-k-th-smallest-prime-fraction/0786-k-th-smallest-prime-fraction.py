class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        
        heap = []
        
        heapq.heappush(heap,(arr[0]/arr[-1],0,len(arr)-1))
        visited = set()
        while 1:
            
            value,i,j = heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if k == 1:
                return [arr[i],arr[j]]
            k -= 1
            
            if i+1 < j :
                heapq.heappush(heap,(arr[i+1]/arr[j],i+1,j))
            if i < j-1:
                heapq.heappush(heap,(arr[i]/arr[j-1],i,j-1))