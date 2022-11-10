class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = deque()
        prev = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+= prev
            answer.appendleft(digits[i]%10)
            prev = digits[i]//10
        if prev != 0:
            answer.appendleft(prev)
        return answer