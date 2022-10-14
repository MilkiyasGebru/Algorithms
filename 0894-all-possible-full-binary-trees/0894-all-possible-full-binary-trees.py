# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0 :
            return []
        def rec(n):
            if n == 1:
                return [TreeNode()]
            ans  =[]
            for i in range(1,n,2):
                a = rec(i)
                b = rec(n-i-1)
                for k in range(len(a)):
                    
                    for j in range(len(b)):
                        node = TreeNode()
                        node.left = a[k]
                        node.right = b[j]
                        ans.append(node)
                        
            return ans
        return rec(n)