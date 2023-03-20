class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        direction = [-1,1]
        
        def isValid(x):
            return x < 0 or x >= len(flowerbed) or (0 <= x < len(flowerbed) and flowerbed[x]==0) 
        
        index =0
        
        while( n > 0 and index < len(flowerbed)):
            
            
            place = flowerbed[index] != 1 and isValid(index-1) and isValid(index+1)  
            
            if place :
                flowerbed[index] = 1
                n-=1 
                index +=2
                continue
                
                
            index +=1   
            
            
        if n==0: return True
        
                                                                     
            