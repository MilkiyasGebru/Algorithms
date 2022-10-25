class TrieNode:
    def __init__(self):
        
        self.children = defaultdict(lambda:None)
        self.isEnd = False
        
class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def addWord(self,word):
        
        node = self.root
        for letter in word:
            
            if node.isEnd :
                return
            
            if  not node.children[letter] :
                node.children[letter]=TrieNode()
                
            node =  node.children[letter]
            
        node.isEnd = True
        
    def findWord(self,word):
        
        successor = []
        node = self.root
        
        for letter in word:
            
            if  node.children[letter] :
                
                successor.append(letter)
                node = node.children[letter]
                
                if node.isEnd:
                    break
            else:
                
                break
        
        return "".join(successor) if node.isEnd else word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        trie = Trie()
        answer = []
        
        for word in dictionary:
            trie.addWord(word)
        
        for word in sentence.split():
            answer.append(trie.findWord(word))
        
        return " ".join(answer)
        
        