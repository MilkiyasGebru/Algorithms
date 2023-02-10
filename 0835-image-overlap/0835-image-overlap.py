class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        points = defaultdict(int)
        answer = 0
        
        for row1 in range(len(img1)):
            
            for col1 in range(len(img1)):
                
                if img1[row1][col1] == 0:
                    continue
                
                for row2 in range(len(img2)):
                    
                    for col2 in range(len(img2)):
                        
                        if img2[row2][col2] == 0:
                            continue
                        
                        points[(row2-row1,col2-col1)] += 1
                        
                        answer = max(answer, points[(row2-row1,col2-col1)])
        
        return answer 
                        