class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        
        z = self.root
        
        for w in word:
            
            if w not in z.children:
                
                z.children[w]=TrieNode()
                
            z= z.children[w]
            
        z.isEnd=True  
        
    def search(self, word: str) -> bool:
        z = self.root
       
        def check(k,z):
            
            
            for i in range(k,len(word)):
                
                if word[i]!='.' and word[i] in z.children:
                    
                    z = z.children[word[i]]
                    
                elif word[i]=='.' and len(z.children.keys())!=0:
                    
                    x = False
                    
                    for key in z.children:
                        
                        x = x or check(i+1,z.children[key])
                        
                    return x   
                
                else:
                    return False
                
            if  z.isEnd:
                return True
            
        return check(0,z)        
        
       
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)