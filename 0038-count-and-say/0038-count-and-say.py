class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        x = self.countAndSay(n-1)
        s = []
        
        prev = x[0]
        count = 1
        
        for i in range(1,len(x)):
            
            if x[i]!=prev :
                
                s.append(str(count))
                s.append(prev)
                
                prev = x[i]
                count = 1
                
            else:
                count+=1
                
        s.append(str(count))
        s.append(prev)
        
        return "".join(s)
        
            