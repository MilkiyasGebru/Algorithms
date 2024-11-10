class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        ans = [0 for _ in range(50)]
        for i in range(len(ans)):
            
            ans[i] += (x  & (1 << i)) != 0
        i = 0
        n -= 1
        while n != 0:
            while ans[i] != 0:
                i += 1
            ans[i] = n%2
            i += 1
            n //= 2
        number = 0
        for i in range(len(ans)):
            if ans[i]:
                number += int(2**(i))
        return number
                
        