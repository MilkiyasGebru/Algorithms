class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self,word):
        node = self.root
        
        for letter in word:
            if node.isEnd :
                return
            if node.children[letter] :
                node = node.children[letter]
            else:
                node.children[letter]=TrieNode()
                node =  node.children[letter]
        node.isEnd = True
        
    def findWord(self,word):
        successor = []
        node = self.root
        for letter in word:
            if node.children[letter] :
                successor.append(letter)
                node = node.children[letter]
                if node.isEnd:
                    return "".join(successor)
            else:
                return word
        if node.isEnd:
            return "".join(successor)
        return word
                
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        trie = Trie()
        answer = []
        for word in dictionary:
            trie.addWord(word)
        
        for word in sentence.split():
            answer.append(trie.findWord(word))
        
        return " ".join(answer)
        
        