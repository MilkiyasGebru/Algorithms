class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        f = defaultdict(int)
        answer = 0
        for t in time:
            answer += f[(60-(t%60))%60]
            f[t%60]+=1
        
        return answer