# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.ans = 0
        def rec(node):
            
            if not node:
                return {}
            
            if not node.left and not node.right:
                return {1:1}
            
            left = rec(node.left)
            right = rec(node.right)
            
            depth = {}
            for left_key in left.keys():
                for right_key in right.keys():
                    
                    if left_key + right_key  <= distance:
                        self.ans += left[left_key] * right[right_key]
            
                depth[left_key+1] = left[left_key]
            for right_key in right.keys():
                if not (right_key+1) in depth.keys():
                    depth[right_key+1] = 0
                depth[right_key+1] += right[right_key]
            return depth
        
        rec(root)
        return self.ans