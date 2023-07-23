# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def rec(left,right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            
            #The possible roots of the graph
            possible_nodes = []
            
            for val in range(left,right+1):
                
                left_nodes = rec(left,val-1)
                right_nodes = rec(val+1,right)
                
                for leftnode in left_nodes:
                    for rightnode in right_nodes:
                        
                        possible_nodes.append(TreeNode(val,leftnode,rightnode))
            
            return possible_nodes
        
        return rec(1,n)
        