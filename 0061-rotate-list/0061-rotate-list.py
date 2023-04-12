# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLength(self,node):
        
        length = 0
        
        while node:
            
            node = node.next
            length += 1
            
        return length
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = self.findLength(head)
        
        if length == 0 :
            return head
        
        k %= length
        start1 = start2 = head
        
        for i in range(k):
            
            start1 = start1.next
            
        while(start1.next):
            
            start2 = start2.next
            start1 = start1.next
            
        start1.next = head
        new_head = start2.next
        start2.next = None
        
        return new_head