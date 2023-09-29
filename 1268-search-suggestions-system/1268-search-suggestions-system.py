class TrieNode:
    
    def __init__(self):
        
        self.children = [ None for _ in range(26)]
        self.isend = False
class TrieTree:
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def add_product(self,product):
        
        curr_node = self.root
        
        for character in product:
            index = ord(character) - ord("a")
            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]
        
        curr_node.isend = True
    
    def traverse(self,product):
        
        curr_node = self.root
        
        for character in product:
            index = ord(character) - ord("a")
            
            if not curr_node.children[index]:
                return []
            
            curr_node = curr_node.children[index]
        suggested_words = []
        self.suggest(curr_node,product,suggested_words)
        
        return suggested_words
    
    def suggest(self,node,pre,answer):
        if len(answer) >= 3:
            return
        
        if node.isend:
            answer.append(pre)
        
        for i in range(26):
            if node.children[i]:
                
                self.suggest(node.children[i],pre+chr(i+ord("a")),answer)
        


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        answer = []
        trie = TrieTree()
        for product in products:
            trie.add_product(product)
        
        
        for i in range(len(searchWord)):
            answer.append(trie.traverse(searchWord[0:i+1]))
        
        return answer