class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        if k > 0:
            start,end = 1,k
        else:
            start,end = len(code)-abs(k),len(code)-1
        window_sum = 0
        for i in range(start,end+1):
            window_sum += code[i]
        
        for i in range(len(code)):
            answer.append(window_sum)
            window_sum -= code[(start)%len(code)]
            window_sum += code[(end+1)%len(code)]
            start += 1
            end += 1
        return answer