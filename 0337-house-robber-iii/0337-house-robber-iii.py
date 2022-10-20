# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def calc(house,steal):
            
            if not house:
                return 0
            if steal == 1:
                return max(house.val + calc(house.left,0) + calc(house.right,0), calc(house.left,1) + calc(house.right,1))
            return calc(house.left,1) + calc(house.right,1)
        return calc(root,1)
            
            
             