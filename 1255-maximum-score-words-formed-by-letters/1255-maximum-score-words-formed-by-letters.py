class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        f = Counter(letters)
        words_dict = []
        
        for word in words:
            words_dict.append(Counter(word))
        self.total = 0
        def backTrack(index,f,total):
            
            if index == len(words):
                self.total = max(self.total, total)
                return 
            isValid = True
            for key in words_dict[index]:
                isValid = isValid and f[key] >= words_dict[index][key]
            
            if isValid :
                value = 0
                for key in words_dict[index]:
                    f[key] -= words_dict[index][key]
                    value += score[(ord(key)-ord("a"))]*words_dict[index][key]
                backTrack(index+1,f,total+value)
                for key in words_dict[index]:
                    f[key] += words_dict[index][key]
            backTrack(index+1,f,total)
        backTrack(0,f,0)
        return self.total
            