class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = num
        num = list(str(num))
        
        for i in range(len(num)):
            
            for j in range(i,len(num)):
                
                num[i], num[j] = num[j], num[i]
                
                max_num = max(max_num , int("".join(num)))
                
                num[i], num[j] = num[j], num[i]
        
        return max_num
        
        
                