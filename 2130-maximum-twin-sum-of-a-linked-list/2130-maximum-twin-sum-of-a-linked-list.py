# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head
        prev = None
        max_answer = 0
        
        while fast and fast.next:
            
            fast = fast.next.next
            save = slow.next
            slow.next = prev
            prev = slow
            slow = save
            
        
        while slow:
            
            max_answer = max(max_answer, slow.val + prev.val)
            prev = prev.next
            slow = slow.next
        
        return max_answer
        