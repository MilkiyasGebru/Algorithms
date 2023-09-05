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
        
        visited = {}
        def copy_node(node):
            
            if not node:
                return None
            
            if node in visited:
                return visited[node]
            
            new_node = Node(node.val)
            visited[node] = new_node
            new_node.next= copy_node(node.next)
            new_node.random = copy_node(node.random)
            
            
            return visited[node]
        
        return copy_node(head)