# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertToList(self,head:Optional[ListNode]):
        
        array = []
        
        while(head):
            
            array.append(head.val)
            head = head.next
            
        return array
    
    def convertToTree(self,array):
        
        if len(array) == 0:
            return None
        
        mid = len(array)//2
        
        return TreeNode(array[mid],self.convertToTree(array[:mid]),self.convertToTree(array[mid+1:]))
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        array = self.convertToList(head)
        return self.convertToTree(array)
        
        