class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        
        for log in logs:
            
            if log == "../":
                operations -= 1
                operations = max(operations,0)
            elif log == "./":
                continue
            else:
                operations += 1
        
        return operations 