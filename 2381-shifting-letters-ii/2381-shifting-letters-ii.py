class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for i in range(len(s)+1)]
        
        for first,last,d in shifts:
            
            prefix[first]+=1 if d == 1 else -1
            prefix[last+1]-=1 if d == 1 else -1
            
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
            
        answer = []
        
        for index,letter in enumerate(s):
            answer.append(chr((prefix[index]+ord(letter)-ord("a"))%26+ord("a")))
            
        return "".join(answer)
            