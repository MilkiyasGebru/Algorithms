# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        start1,end_list2 = list1,list2
        first = second = None
        
        for i in range(b):
            
            if i == a-1:
                first = list1
            
            second = list1
            list1 = list1.next
        
            
        while(end_list2.next):
            end_list2 = end_list2.next
            
        first.next = list2
        end_list2.next = list1.next
        
        return start1