class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        frequency_p = defaultdict(int)
        frequency_s = defaultdict(int)
        
        answer = []
        
        for letter in p:
            frequency_p[letter]+=1
        
        left = 0
        for right in range(len(s)):
            
            frequency_s[s[right]]+=1
            
            while( frequency_s[s[right]] > frequency_p[s[right]]):
                
                frequency_s[s[left]]-=1
                left+=1
            
            if frequency_s[s[right]] == frequency_p[s[right]] and right - left + 1 == len(p):
                
                answer.append(left)
                
        return answer