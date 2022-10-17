class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter(sentence).keys())==26