class Solution:
    def minChanges(self, s: str) -> int:
        
        answer = 0
        for i in range(0,len(s),2):
            ones = (s[i] == "1") + (s[i+1] == "1")
            answer += min(ones, 2 - ones)
        return answer
            