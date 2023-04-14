class Solution:
    def maxProduct(self, s: str) -> int:
        def isPalindrom(path):
            
            arr = []
            for i in range(len(path)):
                if path[i] == '1':
                    arr.append(s[i])
            
            string = "".join(arr)
            return (string != "") and  string == string[::-1]
        possible = []
        def backTrack(index,path):
            
            if index == len(s):
                if isPalindrom(path):
                    possible.append((int(path,2),path.count("1")))
                return
            backTrack(index+1 , path +"1")
            backTrack(index+1, path +"0")
        answer = 0
        backTrack(0,"")
        
        for i in range(len(possible)):
            
            x = possible[i][0]
            count_x = possible[i][1]
            
            for j in range(i+1,len(possible)):
                
                y = possible[j][0]
                count_y = possible[j][1]
                
                if x & y == 0:
                    answer = max(count_y * count_x,answer)
                    
        return answer
        
        