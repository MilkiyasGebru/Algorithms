class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        answer = 1
        for i in range(len(points)):
            lines = defaultdict(int)

            for j in range(len(points)):
                
                if i == j:
                    continue
                
                if points[i][0] == points[j][0]:
                    lines["inf"] += 1
                    answer = max(answer,lines["inf"] + 1)
                else:
                    
                    lines[(points[j][1]-points[i][1])/(points[j][0]-points[i][0])] += 1
                    answer = max(answer,lines[(points[j][1]-points[i][1])/(points[j][0]-points[i][0])] + 1 )
            
        return answer   
                    