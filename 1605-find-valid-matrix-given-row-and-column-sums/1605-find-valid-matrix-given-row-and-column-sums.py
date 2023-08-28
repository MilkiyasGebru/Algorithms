class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        validMatrix = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        
        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                validMatrix[row][col] = min(rowSum[row],colSum[col])
                rowSum[row] -= validMatrix[row][col]
                colSum[col] -= validMatrix[row][col]
        
        return validMatrix