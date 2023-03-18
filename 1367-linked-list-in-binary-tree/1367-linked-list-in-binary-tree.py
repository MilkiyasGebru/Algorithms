# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findPath(self,node,head):
        
        
        if not head:
            return True
        
        if not node:
            return False
        
        if node.val != head.val:
            return False
        
        return self.findPath(node.left,head.next) or self.findPath(node.right,head.next)
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        return self.findPath(root,head) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
        
        