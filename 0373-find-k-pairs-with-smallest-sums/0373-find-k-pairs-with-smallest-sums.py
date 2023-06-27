class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        visited = set()
        
        heap = [[nums1[0]+nums2[0],0,0]]
        
        while k > len(visited) and len(heap) > 0:
            
            total,i,j = heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            
            if (i+1) < len(nums1):
                heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
            if (j+1) < len(nums2):
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        answer = []
        for key in visited:
            answer.append([nums1[key[0]],nums2[key[1]]])
        
        return answer
            
            
            