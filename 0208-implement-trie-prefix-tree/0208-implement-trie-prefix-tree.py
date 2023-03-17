class TrieNode:
    def __init__(self):
        self.children=defaultdict(lambda:None)
        self.isEnd=False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if not node.children[w]:
                node.children[w]=TrieNode()
            node = node.children[w]
        node.isEnd=True    
                
                

    def search(self, word: str) -> bool:
        node=self.root
        for w in word:
            if not node.children[w]:
                return False
            node = node.children[w]
        return node.isEnd==True  
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for w in prefix:
            if not node.children[w]:
                return False
            node = node.children[w]
        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)