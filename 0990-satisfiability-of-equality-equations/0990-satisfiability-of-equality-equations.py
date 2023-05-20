class UnionFind:
    
    def __init__(self):
        
        self.letters = [i for i in range(26)]
    
    def find(self,letter):
        
        if letter == self.letters[letter]:
            return letter
        self.letters[letter] = self.find(self.letters[letter])
        return self.letters[letter]
    
    def union(self,let1,let2):
        
        par1 = self.find(let1)
        par2 = self.find(let2)
        
        if par1 == par2:
            return 
        
        self.letters[par2] = par1
        return

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        graph = UnionFind()
        
        # Only equals
        for i in range(len(equations)):
            if equations[i][1] == "=":
                graph.union(ord(equations[i][0])-ord("a"),ord(equations[i][-1])-ord("a"))
        boolean = True
        for i in range(len(equations)):
            if equations[i][1] == "!":
                boolean = boolean and (graph.find(ord(equations[i][0])-ord("a")) != graph.find(ord(equations[i][-1])-ord("a"))
                                     )
        
        return boolean