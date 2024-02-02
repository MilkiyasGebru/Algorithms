class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        answer = []
        def backTrack(num,last):
            
            if low <= num <= high:
                answer.append(num)
            if num > high:
                return
            if last == 9:
                return
            
            return backTrack(num*10 + last + 1 , last + 1)
        
        for num in range(1,10):
            backTrack(num,num)
        return sorted(answer)
            
            