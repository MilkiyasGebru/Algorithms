class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        original_number = int(n)
        
        self.diff = math.inf
        self.ans = n
        if len(n) > 1 and  n.count("9") == len(n):
            return str(int(n)+2)
        def rec(left,right,s):

            if left > right:

                number = int("".join(s))
                reverse = int(str(number)[::-1])
                
                if number - original_number == 0 or number != reverse:
                    return
                
                if abs(number - original_number) < self.diff:
                    self.ans = "".join(s)
                    self.diff = abs(number - original_number)
                    
                if abs(number - original_number) == self.diff:
                    self.ans = str(min(int("".join(s)),int(self.ans)))
                    
                return
            
            if left == right:
                
                for i in range(10):
                    
                    s[left] = str(i)
                    rec(left+1,right-1,s)
                    
                return 
            
            s[left] = n[left]
            s[right] = n[left]
            rec(left+1,right-1,s)
            
            s[left] = str((int(n[left])+1)%10)
            s[right] = s[left]
            rec(left+1,right-1,s)
            
            s[left] = str((int(n[left])-1)%10)
            s[right] = s[left]
            rec(left+1,right-1,s)
            
            if int("".join(s[0:left+1])) == 0:
                s[right] = "9"
                rec(left+1,right-1,s)
            
        rec(0,len(n)-1,["0" for _ in range(len(n))])
        return self.ans
            