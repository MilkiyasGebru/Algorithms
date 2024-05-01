class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_occurence = 0
        for i in range(len(word)):
            if word[i] == ch:
                first_occurence = i
                break
        return word[0:first_occurence+1][::-1] + word[first_occurence+1:]