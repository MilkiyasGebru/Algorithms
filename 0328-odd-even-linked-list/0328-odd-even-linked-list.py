# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNode = odd = ListNode()
        evenNode= even =ListNode()
        length = 1
        while head :
            if length % 2 :
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            length += 1
        
        even.next = None
        odd.next = evenNode.next
        return oddNode.next
        