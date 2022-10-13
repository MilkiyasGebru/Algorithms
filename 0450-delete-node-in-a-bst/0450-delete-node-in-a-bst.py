# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        parent =TreeNode(-1.5,None,root)
        def leftMost(node):
            if not node.left:
                return node
            return leftMost(node.left)
        def dfs(node,p):
            
            if not node:
                return p
            
            if node.val == key:
                if not node.right:
                    if p.right == node:
                        p.right = node.left
                        return p
                    else:
                        p.left = node.left
                        return p
                else:
                    n = leftMost(node.right)
                    if p.right == node:
                        p.right = node.right
                        n.left = node.left
                        return p
                    else:
                        p.left = node.right
                        n.left = node.left

                        return p
            if node.val > key:
                dfs(node.left,node)
                return p
            else:
                dfs(node.right,node)
                return p
        return dfs(root,parent).right
                    
            