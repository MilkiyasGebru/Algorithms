class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        total_xor = 0
        for num in nums:
            total_xor ^= num
        max_num = (2**maximumBit)-1
        answer =[1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            answer[i] = max_num ^ total_xor
            total_xor ^= nums[-(i+1)]
        return answer