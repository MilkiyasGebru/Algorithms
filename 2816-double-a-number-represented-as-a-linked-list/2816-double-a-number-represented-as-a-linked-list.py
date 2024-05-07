# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode(0,head)
        def rec(node):
            if not node:
                return 0
            
            val = rec(node.next)
            node.val += val + node.val
            val = node.val//10
            node.val %= 10
            return val
        rec(new_head)
        return new_head if new_head.val != 0 else new_head.next