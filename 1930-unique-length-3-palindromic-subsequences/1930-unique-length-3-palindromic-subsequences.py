class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        
        
        position = defaultdict(list)
        for i in range(len(s)):
            position[ord(s[i])].append(i)
        answer = 0
        # return
        for i in range(ord("a"),ord("a")+26):
            if len(position[i]) < 2:
                continue
            for j in range(ord("a"),ord("a")+26):
                
                for index in position[j]:
                    if position[i][0] < index < position[i][-1]:
                        answer += 1
                        break
        return answer
        
        