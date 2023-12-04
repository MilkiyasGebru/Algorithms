class Solution:
    def largestGoodInteger(self, num: str) -> str:
        value = 0
        string = ""
        
        for i in range(len(num)-2):
            
            if num[i] == num[i+1] == num[i+2] and int(num[i:i+3]) >= value:
                value = int(num[i:i+3])
                string = num[i:i+3]
        
        return string
                