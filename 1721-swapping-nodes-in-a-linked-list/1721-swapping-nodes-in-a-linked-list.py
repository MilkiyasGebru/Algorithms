# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []
        
        while(head):
            
            array.append(head)
            head = head.next
        
        array[k-1].val,array[-k].val = array[-k].val,array[k-1].val
        return array[0]
        