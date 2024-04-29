class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        total_xor = k
        for num in nums:
            total_xor ^= num
        
        return bin(total_xor).count("1")
        