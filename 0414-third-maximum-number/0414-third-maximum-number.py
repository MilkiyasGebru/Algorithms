class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        first = second = thrid = None
        
        for num in nums:
            
            if not first or num > first:
                thrid = second
                second = first
                first = num
            elif (not second or num > second) and num != first:
                thrid = second
                second = num
            
            elif (not thrid or num > thrid ) and (num != second and num!= first):
                thrid = num
                
        if thrid != None :
            return thrid
        
        return first