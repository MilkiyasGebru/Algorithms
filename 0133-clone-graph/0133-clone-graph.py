"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def makeGraph(self,node,f):
        
        if not node:
            return None
        
        if node.val not in f:
            
            f[node.val] = Node(node.val)
            
            for neigbour in node.neighbors:
                
                f[node.val].neighbors.append(self.makeGraph(neigbour,f))
            
        return f[node.val]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        return self.makeGraph(node,{})