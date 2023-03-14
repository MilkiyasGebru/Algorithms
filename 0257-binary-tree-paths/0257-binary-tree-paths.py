# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        answer = []
        def rec(node,path,array):
            
            if not node:
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                
                array.append("->".join(path))
            
            rec(node.left,path,array)
            rec(node.right,path,array)
            path.pop()
        
        rec(root,[],answer)
        return answer