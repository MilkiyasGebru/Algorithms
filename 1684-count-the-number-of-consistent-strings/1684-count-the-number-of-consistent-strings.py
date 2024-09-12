class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        answer = 0
        allowedFreq = Counter(allowed)
        for word in words:
            freq = Counter(word)
            length = count = 0
            for key in freq.keys():
                length += 1
                count += 1 if allowedFreq[key] > 0 else 0
            answer += length == count
        return answer
            