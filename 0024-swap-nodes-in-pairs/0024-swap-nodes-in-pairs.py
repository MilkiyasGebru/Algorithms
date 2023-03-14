# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = first_node = ListNode(0,head)
        
        while(head and head.next):
             
            y = head.next
            head.next = head.next.next
            y.next = head
            first_node.next = y
            first_node = head
            head = head.next
            
        return dummy_node.next