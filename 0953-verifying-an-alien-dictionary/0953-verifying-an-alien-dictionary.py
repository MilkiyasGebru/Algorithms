class Solution:
    def compare(self,word1,word2,order):
        
        for i in range(min(len(word1),len(word2))):
            
            if order[word1[i]] < order[word2[i]]:
                return True
            
            elif order[word2[i]] < order[word1[i]]:
                return False
            
        return True if len(word1) <= len(word2) else False
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        num = defaultdict(int)
        
        for i in range(len(order)):
            num[order[i]] = i
            
        answer =True
        
        for i in range(1,len(words)):
            
            answer = answer and self.compare(words[i-1],words[i],num)
        
        
        
        return answer