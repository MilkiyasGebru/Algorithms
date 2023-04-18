class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        stack = []
        for i in range(min(len(word1),len(word2))):
            stack.append(word1[i])
            stack.append(word2[i])
            
        stack.extend(word1[i+1:])
        stack.extend(word2[i+1:])
        
        return "".join(stack)