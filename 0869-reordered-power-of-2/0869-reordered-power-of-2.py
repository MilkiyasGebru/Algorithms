class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        count = defaultdict(int)
        
        for i in (str(n)):
            count[i] += 1
        
        for i in range(31):
            num = str(1<<i)
            count2 = defaultdict(int)
            for j in num:
                count2[j] += 1
            if count == count2:
                return True
        
        return False
            
            