class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        answer = []
        self.backTrack(0,[],s,answer)
        return answer
        
    def backTrack(self,index,path,string,answer):
        
        if index == len(string):
            answer.append("".join(path))
            return
        if string[index].isalpha():
            self.backTrack(index+1,path+[string[index].upper()],string,answer)
            self.backTrack(index+1,path + [string[index].lower()],string,answer)
        else:
            self.backTrack(index+1,path+[string[index]],string,answer)
    
            