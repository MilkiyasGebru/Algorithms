class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x = sorted(s1)
        y = sorted(s2)
        break1 = break2 = True
        
        for i in range(len(x)):
            if y[i] > x[i]:
                break1 = False
            if x[i] > y[i]:
                break2 = False
        
        return break1 or break2