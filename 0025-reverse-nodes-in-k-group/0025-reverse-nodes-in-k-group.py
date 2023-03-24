# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def check(self,head,k):
        
        for _ in range(k):
            if head == None:
                return False
            head = head.next
        return True
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        return self.reverseNodes(head,k)
        
    def reverseNodes(self,inital,k):
        if not self.check(inital,k):
            return inital
        
        head = inital
        prev = None
        for _ in range(k):
            
            node = head.next
            head.next = prev
            prev = head
            head = node
            
        inital.next = self.reverseNodes(head,k)
        return prev
            