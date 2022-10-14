# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if head == slow:
            return None
        if slow.next == None:
            head.next=None
            return head
        slow.val = slow.next.val
        slow.next = slow.next.next
        return head