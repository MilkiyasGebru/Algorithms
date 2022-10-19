# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isValid(self, row, col, matrix):
        
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col]==-1
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        direction = { 0 :(0,1), 1 : (1,0), 2: (0,-1), 3 : (-1,0) }
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.rec(0, 0, matrix, head, 0, direction)

    def rec(self, row, col, matrix, node, arrow, direction):

        matrix[row][col]=node.val

        if node.next == None:

            return matrix

        if self.isValid(row + direction[arrow][0], col + direction[arrow][1], matrix):

            return self.rec(row + direction[arrow][0], col + direction[arrow][1], matrix, node.next, arrow, direction)

        new_arrow = (arrow + 1)%4

        return self.rec(row + direction[new_arrow][0], col + direction[new_arrow][1], matrix, node.next, new_arrow, direction)