# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode(float('inf'),head)
        stack =[dummy_node]
        
        while(head):
            
            while(stack and stack[-1].val < head.val):
                
                node = stack.pop()
            
            stack[-1].next = head
            stack.append(head)
            
            head = head.next
        
        return dummy_node.next