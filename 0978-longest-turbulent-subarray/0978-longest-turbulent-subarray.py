class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        stack = []
        answer = 0
        for i in range(len(arr)):
            
            if stack and stack[-1] == arr[i]:
                stack = []
            elif len(stack) >= 2 and (stack[-2] - stack[-1])*(stack[-1] - arr[i]) > 0:
                stack = [stack[-1]]
            
            
            stack.append(arr[i])
            answer = max(answer,len(stack))
        return answer