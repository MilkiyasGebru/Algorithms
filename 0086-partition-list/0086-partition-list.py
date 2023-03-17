# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(float("-inf"),head)
        
        def rec(node):
            
            if not node.next:
                
                if node.val < x:
                    
                    return node,None 
                
                return None,node
                
            
            less,great = rec(node.next)
            
            if node.val < x:
                
                node.next = less
                return node,great
            
            node.next = great
            
            return less,node
        
        less,great = rec(dummy_node)
        
        head = less
        
        while(less.next):
            
            less = less.next
        
        less.next = great
        return head.next
            