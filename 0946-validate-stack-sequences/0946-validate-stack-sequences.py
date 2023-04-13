class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        visited = set()
        stack = []
        j = 0
        for i in range(len(popped)):
            
            while popped[i] not in visited:
                
                stack.append(pushed[j])
                visited.add(pushed[j])
                j += 1
            
            if stack[-1] != popped[i]:
                return False
            
            stack.pop()
        
        return True