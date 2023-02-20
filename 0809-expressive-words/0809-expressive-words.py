class Solution:
    def convertToList(self,word):
        ans = []
        f = defaultdict(int)
        prev = word[0]
        f[prev]+=1
        for i in range(1,len(word)):
            if word[i] == prev:
                f[prev]+=1
            else:
                ans.append([prev,f[prev]])
                f[prev]=0
                prev = word[i]
                f[prev]=1
        ans.append([word[-1],f[prev]])
        return ans
    def check(self,list1,list2):
        
        if len(list1) != len(list2):
            return 0
        
        for i in range(len(list1)):
            
            if (list1[i][0] != list2[i][0])  or list1[i][1] < list2[i][1] or (list1[i][1] != list2[i][1] and list1[i][1] < 3):
                return 0
        return 1
        
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        list1 = self.convertToList(s)
        answer = 0
        for word in words:
            answer += self.check(list1,self.convertToList(word))
        return answer
        
        