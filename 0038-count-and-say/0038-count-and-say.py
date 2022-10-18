class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        x = self.countAndSay(n-1)
        s = []
        prev = ""
        count = 0
        for i in range(len(x)):
            if x[i]!=prev :
                if prev != "":
                    s.append(str(count))
                    s.append(prev)
                prev = x[i]
                count = 1
            else:
                count+=1
        s.append(str(count))
        s.append(prev)
        
        return "".join(s)
        
            