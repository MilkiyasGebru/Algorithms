class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        answer = 0
        for i in range(len(strs[0])):
            last = "a"
            for j in range(len(strs)):
                
                if strs[j][i] >= last:
                    last = strs[j][i]
                else:
                    answer += 1
                    break
        return answer