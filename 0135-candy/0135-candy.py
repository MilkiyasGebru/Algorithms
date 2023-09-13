class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        left = [1 for _ in range(len(ratings))]
        right = [1 for _ in range(len(ratings))]
        candy_needed = 0
        
        for i in range(1,len(ratings)):
            
            if  ratings[i] > ratings[i-1]:
                left[i] += left[i-1]
                
        for i in range(len(ratings)-2,-1,-1):
            
            if ratings[i] > ratings[i+1]:
                right[i] += right[i+1]
        
        for i in range(len(ratings)):
            
            candy_needed += max(left[i],right[i])
        
        return candy_needed
        