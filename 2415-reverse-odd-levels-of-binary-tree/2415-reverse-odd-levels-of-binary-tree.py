# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        q.append(root)
        level = 0
        def rec():
            left = 0
            right = len(q)-1
            while(left<=right):
                q[left].val,q[right].val=q[right].val,q[left].val
                left+=1
                right-=1
        while(q):
            x = len(q)
            if level%2==1:
                rec()
            for _ in range(x):
                node = q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            level+=1
        return root