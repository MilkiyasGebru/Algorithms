class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k > len(arr):
            return max(arr)
        length = len(arr)
        for i in range(len(arr)):
            arr.append(arr[i])
        answer = [arr[0],0]
        
        for i in range(1,len(arr)):
            
            if arr[i] > answer[0]:
                answer = [arr[i],1]
                
            else:
                answer[-1] += 1
                
            if answer[-1] >= k:
                return answer[0]
        