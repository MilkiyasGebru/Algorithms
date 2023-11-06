class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        
        answer = [arr[0],0]
        
        for i in range(1,len(arr)):
            
            if arr[i] > answer[0]:
                answer = [arr[i],1]
                
            else:
                answer[-1] += 1
                
            if answer[-1] >= k:
                return answer[0]
        return max(answer)