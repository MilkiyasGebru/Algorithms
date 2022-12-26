class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        
        original_array = [1]
        while(len(original_array) < n):
            x = len(original_array)
            for i in range(x):
                original_array.append(original_array[i]*2-1)
                original_array[i] *= 2
        answer = []
        for num in original_array:
            if num <= n:
                answer.append(num)
        return answer
        
        
        
        
        