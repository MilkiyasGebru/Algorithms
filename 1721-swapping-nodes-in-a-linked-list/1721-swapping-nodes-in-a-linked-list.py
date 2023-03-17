# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []
        
        dummy_node = head
        first = second = head
        
        for _ in range(k-1):
            first = first.next 
        saved_node = first
        
        while(saved_node.next):
            saved_node = saved_node.next
            second = second.next
            
        first.val,second.val = second.val,first.val
        return dummy_node
        
        
        