# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def rec(node):
            
            if not node.next:
                return node
            
            right_max = rec(node.next)
            
            if node.val >= right_max.val:
                
                node.next = right_max
                return node
            
            return right_max
        
        return rec(head)
        