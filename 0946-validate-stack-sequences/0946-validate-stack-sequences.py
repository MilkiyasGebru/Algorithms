class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        visited = set()
        stack = []
        left = 0
        
        for i in range(len(popped)):
            if popped[i] in visited:
                if not stack or stack[-1]!=popped[i]:
                    return False
                stack.pop()
            else:
                while(popped[i] not in visited):
                    visited.add(pushed[left])
                    stack.append(pushed[left])
                    left += 1
                stack.pop()
        return True
        