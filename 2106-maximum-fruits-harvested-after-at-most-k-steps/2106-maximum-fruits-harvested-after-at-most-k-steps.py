class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        total_fruit =   0 
        fruits_position = [0 for _ in range(max(fruits[-1][0]+1,startPos + 1))]
        left , right = startPos, min(len(fruits_position)-1,startPos + k)
        
        for i in range(len(fruits)):
            
            fruits_position[fruits[i][0]] += fruits[i][1]
            
            if startPos <=  fruits[i][0] <= startPos + k:
                total_fruit += fruits[i][1]
                
        answer = total_fruit
        while left >= 1 and right >= startPos:
            total_fruit += fruits_position[left-1]
            left -= 1
            
            while( k < 2*min(startPos-left,right-startPos) + max(startPos-left,right-startPos) and right > startPos):

                total_fruit -= fruits_position[right] 
                right -= 1
                
            if k >= 2*min(startPos-left,right-startPos) + max(startPos-left,right-startPos):
                answer = max(answer, total_fruit)
        return answer 
            
            
            