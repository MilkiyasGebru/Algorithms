class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        f = defaultdict(int)
        f["T"] = f["F"] = 0
        left = answer = 0
        for right in range(len(answerKey)):
            
            f[answerKey[right]] += 1
            while min(f.values()) > k:
                f[answerKey[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
        
        return answer