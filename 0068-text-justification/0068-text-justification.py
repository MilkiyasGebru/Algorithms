class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        sentence = []
        answer = []
        count = 0
        
        def builder(words,total_space,last = False):
            
            even = (total_space)//max(1,len(words)-1)
            rem = (total_space)%(max(1,len(words)-1))
            space = " "*even
            
            if last == True or len(words) == 1:
                return (" ".join(words)).ljust(maxWidth)
            
            answer = []
            
            for i in range(len(words)-1):
                
                answer.append(words[i])
                answer.append(space)
                
                if rem > 0:
                    
                    answer.append(" ")
                    rem -= 1
            
            answer.append(words[-1])
            return ''.join(answer)
        
        for word in words:
            
            if count + len(word) + len(sentence)  > maxWidth:
                
                answer.append(builder(sentence,maxWidth - count ))
                sentence = [word]
                count = len(word)
                
            else:
                
                count += len(word)
                sentence.append(word)
                
        answer.append(builder(sentence,maxWidth - count,True))
        return answer