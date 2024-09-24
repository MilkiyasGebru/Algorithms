class Node:
    def __init__(self):
        self.children = defaultdict(lambda : None)
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = Node()
    def addNumber(self,num):
        num = str(num)
        node = self.root
        for n in num:
            if not node.children[n]:
                node.children[n] = Node()
            node = node.children[n]
        node.isEnd = True
    def findNumber(self,num):
        num = str(num)
        node = self.root
        answer = 0
        for i in range(len(num)):
            if not node.children[num[i]]:
                break
            answer += 1
            node = node.children[num[i]]
        return answer
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        trie = Trie()
        answer = 0
        check = Node()
        for num in arr1:
            trie.addNumber(num)
        for num in arr2:
            answer = max(answer,trie.findNumber(num))
        return answer