class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return num
        
        num = num % 9
        
        return num if num != 0 else 9