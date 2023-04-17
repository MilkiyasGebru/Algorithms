class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_ = max(candies)
        answer = [True for _ in range(len(candies))]
        
        for i in range(len(candies)):
            
            if candies[i] + extraCandies < max_:
                
                answer[i] = False
        
        return answer