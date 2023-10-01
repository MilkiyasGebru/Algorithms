class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_element = math.inf
        stack = []
        
        for num in nums:
            
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < stack[-1][0] > num and num > stack[-1][1]:
                return True
            
            stack.append((num,min_element))
            min_element = min(min_element,num)
        
        return False
        