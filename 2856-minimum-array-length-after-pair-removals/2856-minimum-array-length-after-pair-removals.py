class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        '''
        nums[i] should be as maximum as possible while nums[j] should be minimum
        '''
        
        f = defaultdict(int)
        for num in nums:
            f[num] += 1
        heap = []
        for key in f.keys():
            heapq.heappush(heap,-f[key])
        while len(heap) > 1:
            first_max = -1*heapq.heappop(heap) - 1
            second_max = -1*heapq.heappop(heap) - 1
            
            if first_max > 0:
                heapq.heappush(heap,-first_max)
            if second_max > 0:
                heapq.heappush(heap,-second_max)
        
        total = 0
        for length in heap:
            total += -1*length
        
        return total
            
            
            