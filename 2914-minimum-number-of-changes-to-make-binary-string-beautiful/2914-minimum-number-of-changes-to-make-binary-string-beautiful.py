class Solution:
    def minChanges(self, s: str) -> int:
        
        totalOnes = s.count("1")
        totalZeros = len(s) - totalOnes
        leftOnes = leftZeros = 0
        answer = 0
        for i in range(0,len(s),2):
            ones = (s[i] == "1") + (s[i+1] == "1")
            answer += min(ones, 2 - ones)
        return answer
            