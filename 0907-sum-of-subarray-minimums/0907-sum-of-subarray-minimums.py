class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        left = defaultdict(int)
        right = defaultdict(int)
        mod = 10**9 + 7
        stack = []
        for i in range(len(arr)):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                
                count += stack.pop()[1]
                
            
            left[i] = count
            stack.append((arr[i],count))
        stack = []
        for i in range(len(arr)-1,-1,-1):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i],count))
        answer = 0
        for i in range(len(arr)):
            answer += (left[i]*right[i])*arr[i]
            answer %= mod
        return answer