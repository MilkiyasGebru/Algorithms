"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        f = defaultdict(int)
        
        def dfs(node):
            
            if node == None:
                return None
            if f[node] != 0:
                return f[node]
            new_node = Node(node.val)
            f[node] = new_node
            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)
            return f[node]
        
        return dfs(head)
            