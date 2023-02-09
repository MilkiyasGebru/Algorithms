class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = set()
        
        def backTrack(index,path):
            
            if len(path) > 4:
                return
            
            if index == len(s):
                
                if len(path) == 4:
                    answer.add(".".join(path))
                return
            
            if path != [] and (int(path[-1] + s[index]) > 255 or path[-1] == "0"):
                backTrack(index+1,path + [s[index]])
                return
            
            backTrack(index+1,path + [s[index]])
            
            if path:
                
                poped = path.pop()
                backTrack(index+1,path + [poped + s[index]])
                
            else:
                
                backTrack(index+1,[s[index]])
        
        backTrack(0,[])
        
        return answer
            
            