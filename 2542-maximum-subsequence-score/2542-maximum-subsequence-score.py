class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        for i in range(len(nums1)):
            nums1[i] = (nums2[i],nums1[i])
        heap = []
        total_heap = 0
        nums1.sort()
        answer = 0
        for i in range(len(nums1)-1,-1,-1):
            if len(heap) == k-1:
                
                answer = max(answer,(total_heap+nums1[i][1])*nums1[i][0])
                heappush(heap,nums1[i][1])
                num = heappop(heap)
                total_heap += nums1[i][1] - num
            
            else:
                heappush(heap,nums1[i][1])
                total_heap += nums1[i][1]
        
        return answer