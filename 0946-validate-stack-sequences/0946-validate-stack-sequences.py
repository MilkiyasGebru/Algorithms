class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(popped)):
            
            while (not stack or stack[-1] != popped[i]) and j < len(pushed):
                
                stack.append(pushed[j])
                j += 1
            
            if stack[-1] == popped[i]:
            
                stack.pop()
        
        return len(stack) == 0