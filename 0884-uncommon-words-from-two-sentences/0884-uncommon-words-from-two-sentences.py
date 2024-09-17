class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        freq1 = Counter(s1.split(" "))
        freq2 = Counter(s2.split(" "))
        answer = []
        for key in freq1.keys():
            if freq1[key] + freq2[key] == 1:
                answer.append(key)
        for key in freq2.keys():
            if freq1[key] + freq2[key] == 1:
                answer.append(key)
        return answer
        