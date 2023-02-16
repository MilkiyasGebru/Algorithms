class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        answer = []
        f = defaultdict(int)
        changed.sort()
        for num in changed:
            f[num]+=1
        
        for num in changed:
            if f[num] > 0:
                
                f[num]-=1
                if f[2*num] == 0:
                    return []
                answer.append(num)
                f[2*num]-=1
        
        return answer