class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        bit_mask = 0
        answer = []
        for num in nums:
            if bit_mask & (1<<num) == 0:
                bit_mask ^= (1 << num)
            else:
                answer.append(num)
        for k in range(1,len(nums)+1):
            if bit_mask & (1<<k) == 0:
                answer.append(k)
        return answer
        