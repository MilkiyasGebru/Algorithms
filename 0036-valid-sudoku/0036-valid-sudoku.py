class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        Row = defaultdict(set)
        Col = defaultdict(set)
       
        cells= defaultdict(set)
        

                        
        for row in range(9):
            
            for col in range(9):
                
                if board[row][col]!=".":
                    
                    if board[row][col] in cells[(row//3,col//3)] or board[row][col] in Row[row] or board[row][col] in Col[col]:
                        
                        return False
                    
                    cells[(row//3,col//3)].add(board[row][col])
                    Row[row].add(board[row][col])
                    Col[col].add(board[row][col])
                    
       
        return True
            