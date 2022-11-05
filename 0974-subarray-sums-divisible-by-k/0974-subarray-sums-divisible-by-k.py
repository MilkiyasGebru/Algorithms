class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        f = defaultdict(int)
        f[0]=1
        total = 0
        answer = 0
        
        for num in nums:
            total += num
            answer += f[total%k]
            f[total%k]+=1
        return answer
            