# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        q = deque([root])
        
        while q:
            
            size = len(q)
            level_score = 0
            for _ in range(size):
                node = q.popleft()
                level_score += node.val
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            values.append(level_score)
        values.sort()
        if len(values) < k:
            return -1
        return values[-k]
                