class Solution:
    def numSplits(self, s: str) -> int:
        
        forward_letters = []
        backward_letters = []
        
        visited = set()
        for i in s:
            visited.add(i)
            forward_letters.append(len(visited))
        visited = set()
        for i in range(len(s)-1,-1,-1):
            visited.add(s[i])
            backward_letters.append(len(visited))
        good_splits = 0
        for left in range(len(s)-1):
            if forward_letters[left] == backward_letters[len(s)-left-2]:
                good_splits += 1
        return good_splits