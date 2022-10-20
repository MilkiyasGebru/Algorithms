class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0
        
        for i in range(len(popped)):
            
            while( j < len(pushed) and (not stack or stack[-1] != popped[i])):
                
                stack.append(pushed[j])
                j+=1
                
            if stack and stack[-1] == popped[i]:
                stack.pop()
                
        return stack==[]
        