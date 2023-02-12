# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0,None)
        header=head
        carry=0
        while(l1 and l2):
            header.val=l1.val + l2.val + carry
            carry = header.val//10
            header.val %=10
            l1=l1.next
            l2=l2.next
            if (l1 and l2):
                header.next = ListNode(0,None)
                header=header.next
        while(l1 ):
            header.next=ListNode(0,None)
            header=header.next
            header.val = l1.val+carry
            l1=l1.next
            carry = header.val//10
            header.val %=10
            # if l1 == None:
            #     break
            # header.next=ListNode(0,None)
            # header=header.next
        while(l2 ):
            header.next=ListNode(0,None)
            header=header.next
            header.val = l2.val+carry
            l2=l2.next
            carry = header.val//10
            header.val %=10
            # if l2 == None:
            #     break
            # header.next=ListNode(0,None)
            # header=header.next
        if(not carry==0):
            header.next=ListNode(carry,None)
            return head
        else:
            return head
         
            
            