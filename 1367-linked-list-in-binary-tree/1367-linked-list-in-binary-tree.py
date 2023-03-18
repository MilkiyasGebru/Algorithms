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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        self.head2 = head
        @lru_cache(None)
        def rec(node,linkedHead):
            
            if not linkedHead:
                return True
            if not node:
                return False
            
            if linkedHead.val == node.val:
                return rec(node.left,linkedHead.next) or rec(node.right,linkedHead.next) or rec(node.left,self.head2) or rec(node.right,self.head2)
            
            return  rec(node.left,self.head2) or rec(node.right,self.head2)
        
        return rec(root,head)