class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = math.inf
        left = 0
        bits = [0 for _ in range(32)]
        for right in range(len(nums)):
            value = 0
            for i in range(len(bits)):
                bits[i] += (nums[right] &(1 << i)) != 0
                if bits[i]:
                    value |= (1 << i)
            while right >= left and value >= k:
                answer = min(right - left + 1,answer)
                value = 0
                for i in range(len(bits)):
                    bits[i] -= (nums[left] & (1 << i)) != 0
                    if bits[i]:
                        value |= (1 << i)
                left += 1
        return answer if answer != math.inf else -1