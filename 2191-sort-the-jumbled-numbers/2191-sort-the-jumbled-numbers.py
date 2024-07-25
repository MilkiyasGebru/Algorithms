class Solution:
    
    def sort_function(self,num, f):
        num = str(num)
        total = 0
        
        for i in range(len(num)-1,-1,-1):
            total += f[int(num[i])]*(10**(len(num)-i-1))
        return total
    
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        f = {}
        for i in range(len(mapping)):
            f[i]=mapping[i]
        nums.sort(key= lambda num:self.sort_function(num,f))
        
        return nums
