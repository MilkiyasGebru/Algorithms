class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        for i in range(0,len(row),2):
            
            value_needed = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            
            for j in range(i+1,len(row)):
                
                if row[j] == value_needed:
                    
                    break
            
            swaps += 1 if i+1 != j else 0
            row[i+1],row[j] = row[j],row[i+1]
        
        return swaps
            
            
        