class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        total = 0
        op = 0
        total_sum = sum(nums)/2
        for num in nums:
            heapq.heappush(heap,-1*num)
        while( total < total_sum):
            op += 1
            num = -1 * heapq.heappop(heap)
            total += num/2
            heapq.heappush(heap,-1 * num/2)
        return op
        