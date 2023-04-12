class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        if k > 1:
            return "".join(sorted(s))
        q = deque()
        for i in s:
            q.append(i)
        
        answer = "".join(q)
        for i in range(len(s)-1):
            letter = q.popleft()
            q.append(letter)
            answer = min(answer,"".join(q))
        return answer