# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def nodeCopier(self,node):
    #     if node == None:
    #         return None
    #     newNode = TreeNode(0,self.nodeCopier(node.left),self.nodeCopier(node.right))
    #     return newNode
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n % 2 == 0:
            return []
        
        def dp(n):
            if n == 1:
                return [TreeNode(0)]
            nodes = []
            for i in range(1,n,2):
                leftNodes = dp(i)
                rightNodes = dp(n-1-i)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        nodes.append(TreeNode(0,leftNode,rightNode))
            
            return nodes
        
        return dp(n)
                