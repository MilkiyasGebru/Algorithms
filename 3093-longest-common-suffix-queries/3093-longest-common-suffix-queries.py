class Node:
    
    def __init__(self,index=math.inf,length = math.inf):
        self.children = defaultdict(lambda : None)
        self.index = index
        self.length = length
class Trie:
    def __init__(self):
        self.root = Node()
    def addWord(self,word,index):
        node = self.root
        if node.length > len(word):
            node.index = index
            node.length = len(word)
        for w in word:
            if not node.children[w]:
                node.children[w] = Node()
            node = node.children[w]
            if node.length > len(word):
                node.index = index
                node.length = len(word)
            
    def findWord(self,word):
        node = self.root
        for w in word:
            if not node.children[w]:
                break
            node = node.children[w]
        return node.index
        


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        trie = Trie()
        for i in range(len(wordsContainer)):
            trie.addWord(wordsContainer[i][::-1],i)
        answer = []
        
        for word in wordsQuery:
            answer.append(trie.findWord(word[::-1]))
        return answer        
        