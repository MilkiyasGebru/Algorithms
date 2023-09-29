class TrieNode:
    
    def __init__(self):
        
        self.count = 0
        self.children = [ None for _ in range(26)]
    
class TrieTree:
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self,word):
        curr_node = self.root
        
        for character in word:
            index = ord(character) - ord("a")
            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]
            curr_node.count += 1
            
    def calculate_prefix(self,word):
            curr_node = self.root
            total_score = 0
            for character in word:
                index = ord(character) - ord("a")
                curr_node = curr_node.children[index]
                total_score += curr_node.count
            
            return total_score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = TrieTree()
        answer = []
        for word in words:
            trie.addWord(word)
        for word in words:
            answer.append(trie.calculate_prefix(word))
        
        return answer