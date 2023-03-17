# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        firstPoint = lastPoint = -1
        answer = [inf,-1]
        i = 1
        prev = head
        head = head.next
        
        while(head.next):
            
            
            
            if (prev.val > head.val and head.next.val > head.val) or (prev.val < head.val and head.next.val < head.val):
                

                if firstPoint == -1:

                    firstPoint = lastPoint = i

                else:

                    answer[0] = min(i - lastPoint,answer[0])
                    answer[1] = i - firstPoint

                    lastPoint = i
                        
            i+=1
            prev = head
            head = head.next
            
        if answer[0] == inf:
            answer[0] = -1
            
        return answer