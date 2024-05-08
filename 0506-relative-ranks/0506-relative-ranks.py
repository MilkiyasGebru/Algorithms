class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(score[i],i) for i in range(len(score))]
        answer = ["" for _ in range(len(score))]
        
        score.sort(reverse=True)
        
        for i  in range(len(score)):
            
            if i == 0:
                answer[score[i][-1]] = "Gold Medal"
            elif i == 1:
                answer[score[i][-1]] = "Silver Medal"
            elif i == 2:
                answer[score[i][-1]] = "Bronze Medal"
            else:
                answer[score[i][-1]] = str(i+1)
        
        return answer
        