class Solution:
    
    def calculate_num(self,word):
        num = 0
        for letter in word:
            num |= (1 << (ord(letter) - ord("a")))
        
        return num
    
    def maxProduct(self, words: List[str]) -> int:
        
        max_length = 0
        dp = [self.calculate_num(words[i]) for i in range(len(words))]
        
        for i in range(len(words)-1):
            
            # num1 = self.calculate_num(words[i])
            
            for j in range(i+1,len(words)):
                
                # num2 = self.calculate_num(words[j])
                
                if dp[i] & dp[j] == 0:
                    
                    max_length = max(max_length, len(words[i])*len(words[j]))
        
        return max_length