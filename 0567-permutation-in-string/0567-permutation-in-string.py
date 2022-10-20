class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        string1 = defaultdict(int)
        string2 = defaultdict(int)

        for letter in s1:
            string1[letter]+=1
        
        left = 0
        for right in range(len(s2)):
            
            string2[s2[right]]+=1
            
            while(string2[s2[right]] > string1[s2[right]]):
                
                string2[s2[left]]-=1
                left += 1
                
            if string2[s2[right]]==string1[s2[right]] and right - left +1 == len(s1):
                
                return True
            
        return False
        